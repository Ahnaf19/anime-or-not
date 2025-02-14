from fastapi import APIRouter

# from app.schemas.model_schema import GuestBase, GuestData, UpdateGuest
# from app.services.guest_service import GuestService

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/model", tags=["model"])

# Initiate the GuestService with dummy data
# guest_service = GuestService(dummy_guest_data)


# Define the routes
# @router.get("/health", response_model=GuestData)
# async def read_guests() -> GuestData:
#     """
#     Retrieve all guests.

#     Returns:
#         GuestData: A list of all guests.
#     """
#     return guest_service.dummy_guest_data
