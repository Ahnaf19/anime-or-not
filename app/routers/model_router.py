from fastapi import APIRouter, File, UploadFile

from app.schemas.model_schema import ModelHealthResponse, ModelInfoResponse, ModelPredictionResponse
from app.services.model_service import ModelService

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/model", tags=["model"])

# Initialize the model service
model_service = ModelService()


# Define the routes
@router.get("/health", response_model=ModelHealthResponse)
async def read_health() -> ModelHealthResponse:
    """
    check if the model service is running.

    Returns:
    - ModelHealthResponse: A dictionary containing the status of the service.
    """
    return model_service.check_api_status()


@router.get("/model-info", response_model=ModelInfoResponse)
async def read_info() -> ModelInfoResponse:
    """
    Returns the model name

    Returns:
    - ModelInfoResponse: A dictionary containing the model information.
    """
    return model_service.get_model_info()


@router.post("/predict", response_model=ModelPredictionResponse)
async def predict(file: UploadFile = File(...)) -> ModelPredictionResponse:
    """
    Endpoint to make a prediction based on the uploaded file.

    Args:
        file (UploadFile): The file to be used for making the prediction.

    Returns:
        ModelPredictionResponse: The prediction result from the model.
    """
    return await model_service.make_prediction(file)
