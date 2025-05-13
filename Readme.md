
# PikaStyle 🎨😃🤖  
An interactive AI-powered web application for artistic image stylization, emotional analysis, and intelligent conversation.

---

## 📌 Overview  
PikaStyle combines three powerful AI models into a seamless Gradio interface:

- 🎨 Neural Style Transfer (NST): Transforms your content image using the artistic style of another.
- 😃 Facial Expression Recognition (FER): Analyzes the resulting image to detect emotions.
- 🤖 Grookey Chatbot: A conversational AI assistant integrated into the UI.

---

## 🎯 Features

### 🖼️ Stylo Tab (NST + FER)
- Upload a Content Image and a Style Image.
- Apply Neural Style Transfer to generate an artistic output.
- Run Facial Expression Recognition on the stylized image to detect:
  - 😃 Happy, 😢 Sad, 😐 Neutral, 😠 Angry, 😨 Fear, 😲 Surprise, 🤢 Disgust
- Displays both the stylized image and detected emotion.

### 💬 Grookey Tab (AI Chatbot)
- Text-based chatbot interface powered by GPT4Free (Grok model).
- Maintains multi-turn conversation history.
- "Clear" button resets the session.

---

## 🚀 Tech Stack

| Layer       | Tool/Framework                  |
|-------------|----------------------------------|
| Frontend    | Gradio with custom CSS           |
| NST Engine  | PyTorch-based pre-trained model  |
| FER Model   | CNN trained on facial dataset    |
| Chatbot     | GPT4Free (Grok integration)      |
| Deployment  | Localhost / Gradio Share Link    |

---

## 📂 Project Structure

```plaintext
.
├── apply_nst.py             # Style Transfer logic
├── fer_analysis.py          # Emotion Detection logic
├── gradio_app.py            # Gradio UI integration
├── requirements.txt         # Project dependencies
├── .gitattributes           # Git LFS tracking
├── README.md                # Project documentation
└── assets/                  # Demo and media files
    ├── demo1.png
    └── demo2.png
```

---

## 🔧 Installation

📌 Note: This project uses Git LFS for large files (e.g., models, demo assets). Install it before cloning:

```bash
# Step 1: Install Git LFS (if not already installed)
git lfs install

# Step 2: Clone the repository
git clone https://github.com/Akash8002/PikaStyle.git
cd PikaStyle

# Step 3: Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# OR
source venv/bin/activate     # macOS/Linux

# Step 4: Install dependencies
pip install -r requirements.txt
```

---

## 📁 Dataset (For FER Model)

Download and organize the Facial Expression Recognition dataset from Kaggle as follows:

```plaintext
dataset/
├── train/
│   ├── happy/
│   ├── sad/
│   ├── neutral/
│   ├── angry/
│   ├── fear/
│   ├── surprise/
│   └── disgust/
└── validation/
    └── (same structure as train)
```

---

## ⚙️ Usage

Run the Gradio application locally:

```bash
python gradio_app.py
```

The interface will auto-launch in your browser. Use:

- 🖼️ Stylo Tab: Upload content + style image, click “Process”.
- 💬 Grookey Tab: Chat freely with Grookey AI.

---

## 🧠 How It Works

1. 🖌️ Neural Style Transfer:
   - Merges content & style using pre-trained deep learning.
   - Output saved as stylized image.

2. 😃 Emotion Detection:
   - CNN model scans the stylized face.
   - Predicts the dominant facial emotion.

3. 🤖 Grookey Chatbot:
   - Sends user input to GPT4Free API.
   - Generates contextual replies and updates the chat log.

---

## 🛠️ Future Improvements

- Add live webcam input for real-time processing.
- Upgrade style transfer with AdaIN or FastNST.
- Improve chatbot memory and accuracy.
- Replace Grok backend with OpenAI/Gemini/GGUF for local inference.

---

## 🤝 Contributing

Pull requests are welcome! To contribute:

1. Fork the repo
2. Create a new branch (e.g. feature/new-feature)
3. Commit changes
4. Push to your fork
5. Open a Pull Request

---

## 📄 License

This project is licensed under the GNU General Public License v3.0 — see the [LICENSE](LICENSE) file.

---

## 🌟 Support This Project

If you found this useful, please ⭐ the repo. Your support motivates more innovation!

---

## 🙏 Acknowledgments

- GPT4Free for chatbot backend
- Gradio for the UI framework
- Kaggle contributors for the FER dataset

---

🧠 Explore the intersection of Art, Emotion, and AI Conversation with PikaStyle!
