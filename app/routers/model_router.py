from fastapi import APIRouter

# from app.schemas.model_schema import GuestBase, GuestData, UpdateGuest
# from app.services.guest_service import GuestService

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/model", tags=["model"])

# Initiate the GuestService with dummy data
# guest_service = GuestService(dummy_guest_data)


# Define the routes
@router.get("/health", response_model=dict[str, str])
async def read_health() -> dict[str, str]:
    """
    check if the model service is running.

    Returns:
    - dict[str, str]: A dictionary containing the status of the service.
    """
    return {"status": "Model service is running"}
    # """
    # return guest_service.dummy_guest_data

@router.get("/model-info", response_model=dict[str, str])
async def read_info() -> dict[str, str]:
    """
    Returns the model name

    Returns:
    - dict[str, str]: A dictionary containing the model name.
    """
    return {"model": "ResNet50"}