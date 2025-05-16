from PIL import Image
import torch
from torch import nn
from torchvision import transforms
import timm


# create the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# create the function for loading model
def get_model(model_path: str = "animal_model.pth", device=device):
  model = None
  model = torch.load(model_path, map_location=device, weights_only=False)
  model = model.to(device)
  if model:
    print(f'Model loaded successfully: classifier structure: {model.classifier}')

  return model


# setup the transform
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((220,220)),
    transforms.RandomHorizontalFlip(p=0.4),
    transforms.ColorJitter(brightness=0.2, contrast=0.3, saturation=0.2,
                           hue=0.1),
    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])

def predict_image(image_path):
  model = get_model()
  softmax = nn.Softmax(dim=1)
  image_input = Image.open(image_path).convert("RGB")
  image = transform(image_input).unsqueeze(0).to(device)
  with torch.no_grad():
    model.eval()
    preds = model(image)
    preds = softmax(preds)
    prob, preds = torch.max(preds, 1)
  
  # create a list of animal names
  animal_list = ['bear','horse','kangaroo','0wl','whale']
  return animal_list[preds.item()], round(prob.item(), 2)


if __name__ == "__main__":
  print(predict_image(image_path="test.jpg"))