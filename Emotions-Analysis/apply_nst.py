import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import cv2

# Load the NST model
model = torch.hub.load('pytorch/vision:v0.10.0', 'vgg19', pretrained=True).features
model.eval()

# Function to load and preprocess images
def load_image(image_path, size=512):
    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor()
    ])
    return transform(image).unsqueeze(0)

# Function to save the output image
def save_image(tensor, output_path):
    image = tensor.squeeze().detach().cpu().numpy()
    image = np.transpose(image, (1, 2, 0))  # Convert from CHW to HWC
    image = (image * 255).astype(np.uint8)
    cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

# Function to apply NST
def apply_nst(content_path, style_path, output_path):
    content_img = load_image(content_path)
    style_img = load_image(style_path)

    # Apply NST logic (simplified)
    output = content_img * 0.5 + style_img * 0.5

    # Save the stylized image
    save_image(output, output_path)

    return output_path
