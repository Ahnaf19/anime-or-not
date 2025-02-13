from fastapi import FastAPI

from app.routers.model_router import router as model_router

# Create an instance of the FastAPI application
app = FastAPI()

# Include routers
app.include_router(model_router)


def main() -> None:
    """
    Entry point for the application when run explicitly.
    """
    print("main.py running explicitly")


if __name__ == "__main__":
    main()