from transformers import AutoModelForImageClassification, AutoProcessor
from PIL import Image
import torch

# Load the pre-trained model
model_name = "dima806/facial_emotions_image_detection"
model = AutoModelForImageClassification.from_pretrained(model_name)

# Load the image processor
processor = AutoProcessor.from_pretrained(model_name)

def predict_emotion(image_path):
    # Load the image
    image = Image.open(image_path).convert("RGB")
    
    # Preprocess the image
    inputs = processor(images=image, return_tensors="pt")
    
    # Get model predictions
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Convert logits to probabilities
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
    # Get the predicted emotion
    predicted_class = torch.argmax(probabilities, dim=-1).item()
    
    # Emotion labels from Hugging Face model
    emotion_labels = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
    
    return emotion_labels[predicted_class], probabilities.tolist()

# Test the function with an image
image_path = "smile.jpg"  # Replace with your image path
emotion, probs = predict_emotion(image_path)
print(f"Predicted Emotion: {emotion}")
