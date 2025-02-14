from deepface import DeepFace
import cv2

# Function to detect emotions
def detect_emotion(image_path):
    img = cv2.imread(image_path)
    analysis = DeepFace.analyze(img, actions=["emotion"], enforce_detection=False)
    return analysis[0]["dominant_emotion"]

# Example Usage:
# emotion = detect_emotion("stylized_output.jpg")
# print("Detected Emotion:", emotion)
