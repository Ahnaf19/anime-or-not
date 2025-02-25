from enum import Enum

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


class DeviceType(Enum):
    """
    Enum class to represent different types of devices that can be used for computation.

    Attributes:
        CPU (str): Represents the CPU device type.
        CUDA (str): Represents the CUDA (GPU) device type.
        AUTO (str): Automatically selects the appropriate device type based on availability.
    """

    CPU = "cpu"
    CUDA = "cuda"
    AUTO = "auto"
