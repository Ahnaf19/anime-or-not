from enum import Enum
from typing import Optional, Tuple

import torch
from PIL import Image
from torchvision import models, transforms


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


def make_pred(
    img=None,
    image_path: str = r"D:\self_development\coding\python\fastapi\projects\anime-or-not\notebooks\test_img\naruto.jpeg",
    device: DeviceType = DeviceType.AUTO,
    image_size: Tuple[int, int] = (224, 224),
    model: torch.nn.Module | None = None,
    transform: Optional[transforms.Compose] = None,
):
    torch.manual_seed(42)
    torch.cuda.manual_seed(42)

    if device == DeviceType.AUTO:
        device = DeviceType.CUDA if torch.cuda.is_available() else DeviceType.CPU

    class_names = ["Anime", "Cartoon"]

    if model is None:
        model = models.resnet50()
        model.fc = torch.nn.Linear(in_features=model.fc.in_features, out_features=len(class_names), bias=True)
        model.load_state_dict(torch.load("deep_learning_model/models/model-run4.pth"))

    if img is None:
        img = Image.open(image_path).convert("RGB")

    if transform is not None:
        image_transform = transform
    else:
        image_transform = transforms.Compose([transforms.Resize(image_size), transforms.ToTensor()])

    model.to(device.value)
    model.eval()
    with torch.inference_mode():
        transformed_image = image_transform(img).unsqueeze(dim=0)  # type: ignore
        target_image_pred = model(transformed_image.to(device.value))

    target_image_pred_probs = torch.softmax(target_image_pred, dim=1)
    target_image_pred_label = torch.argmax(target_image_pred_probs, dim=1)

    predicted_label = class_names[target_image_pred_label]
    predicted_prob = round(target_image_pred_probs.max().item(), 3)

    return predicted_label, predicted_prob


if __name__ == "__main__":
    predicted_label, predicted_probs = make_pred()
    print(predicted_label, predicted_probs)
