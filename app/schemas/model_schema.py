from pydantic import BaseModel


class ModelHealthResponse(BaseModel):
    status: str
    code: int


class ModelInfoResponse(BaseModel):
    model_name: str
    model_version: str
    model_size: str
    model_parameters: int


class ModelPredictionResponse(BaseModel):
    predicted_label: str
    predicted_prob: float
