import io

import torch
from fastapi import File, HTTPException, UploadFile
from PIL import Image
from torchvision import models

from app.exceptions.custom_exceptions import InvalidImageFileException
from app.schemas.model_schema import ModelHealthResponse, ModelInfoResponse, ModelPredictionResponse
from deep_learning_model.prediction import make_pred


class ModelService:
    def __init__(self):
        model = models.resnet50()
        model.fc = torch.nn.Linear(in_features=model.fc.in_features, out_features=2, bias=True)
        model.load_state_dict(torch.load("deep_learning_model/models/model-run4.pth"))

        self.model = model
        self.total_params = sum(p.numel() for p in self.model.parameters())
        self.model_size = sum(p.element_size() * p.numel() for p in self.model.parameters()) / (1024**2)

    def check_api_status(self) -> ModelHealthResponse:
        try:
            # Perform a simple operation to check if the model is ready
            _ = self.model(torch.randn(1, 3, 224, 224))
            return ModelHealthResponse(status="API is ready for serving model predictions", code=200)
        except Exception as e:
            raise HTTPException(status_code=503, detail="Service Unavailable: " + str(e))

    def get_model_info(self) -> ModelInfoResponse:
        model_info = {
            "model_name": "resnet50",
            "model_version": "1.0",
            "model_size": f"{self.model_size:.2f} MB",
            "model_parameters": self.total_params,
        }

        return ModelInfoResponse(**model_info)

    async def make_prediction(self, file: UploadFile = File(...)):
        if file.content_type is None or not file.content_type.startswith("image/"):
            raise InvalidImageFileException

        contents = await file.read()
        img = Image.open(io.BytesIO(contents)).convert("RGB")

        try:
            predicted_label, predicted_probs = make_pred(img=img)
            return ModelPredictionResponse(predicted_label=predicted_label, predicted_prob=predicted_probs)
        except Exception as e:
            raise HTTPException(status_code=503, detail="Service Unavailable: " + str(e))
