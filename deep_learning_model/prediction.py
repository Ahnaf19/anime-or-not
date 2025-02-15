from typing import List, Optional, Tuple

import torch
from PIL import Image
from torchvision import models, transforms


def make_pred(
    model: torch.nn.Module,
    image_path: str,
    class_names: List[str],
    device: str,
    image_size: Tuple[int, int] = (224, 224),
    transform: Optional[transforms.Compose] = None,
):

    img = Image.open(image_path)

    if transform is not None:
        image_transform = transform
    else:
        image_transform = transforms.Compose([transforms.Resize(image_size), transforms.ToTensor()])

    model.to(device)
    model.eval()
    with torch.inference_mode():
        transformed_image = image_transform(img).unsqueeze(dim=0)  # type: ignore
        target_image_pred = model(transformed_image.to(device))

    target_image_pred_probs = torch.softmax(target_image_pred, dim=1)
    target_image_pred_label = torch.argmax(target_image_pred_probs, dim=1)

    return class_names[target_image_pred_label], target_image_pred_probs


torch.manual_seed(42)
torch.cuda.manual_seed(42)

device = "cuda" if torch.cuda.is_available() else "cpu"
class_names = ["Anime", "Cartoon"]
output_shape = len(class_names)

model = models.resnet50()
model.fc = torch.nn.Linear(in_features=model.fc.in_features, out_features=len(class_names), bias=True)

model.load_state_dict(torch.load("models/model-run4.pth"))
