# PikaStyle
# 🎨 Neural Style Transfer & 😃 Facial Expression Recognition with 🤖 Grookey AI Chatbot  

**An interactive web application that lets you stylize images, analyze emotions, and chat with an AI assistant!**  

---

## **📌 Overview**  
This project integrates three advanced AI functionalities into one cohesive Gradio-based web application:  
- **Neural Style Transfer (NST):** Stylize content images using artistic styles.  
- **Facial Expression Recognition (FER):** Detects human emotions from the stylized image.  
- **Grookey AI Chatbot:** Interactive AI assistant for conversations.  

---

## **🎯 Features**  
1. **Stylo Tab (NST & FER):**  
   - Upload a **Content Image** and a **Style Image**.  
   - Apply **Neural Style Transfer** to blend the two images.  
   - **Facial Expression Recognition** is performed on the stylized image to detect emotions:  
     - 😃 Happy, 😢 Sad, 😐 Neutral, 😠 Angry, 😨 Fear, 😲 Surprise, 🤢 Disgust.  
   - The **Detected Emotion** is displayed along with the stylized image.  

2. **Grookey Tab (AI Chatbot):**  
   - 🤖 Conversational AI powered by the Grok model (via GPT4Free).  
   - Maintains a **Chat History** for a continuous conversation flow.  
   - A **Clear Button** is provided to reset the chat history.  

---

## **🚀 Tech Stack**  
- **Frontend:** Gradio UI with custom CSS for a user-friendly interface.  
- **Backend:**  
  - **Neural Style Transfer**: Deep Learning models (`apply_nst()` function).  
  - **Facial Expression Recognition**: Convolutional Neural Network (CNN).  
  - **AI Chatbot**: GPT4Free integration using **Grok model**.  
- **Deployment:**  
  - Hosted locally with the option to share via a public URL.  
  - **Auto-launches** in the default browser.  

---

## **📂 Project Structure**  
```plaintext
.
├── apply_nst.py             # Neural Style Transfer logic
├── fer_analysis.py          # Facial Expression Recognition logic
├── gradio_app.py            # Main Gradio UI Application
├── README.md                # Project Documentation
├── requirements.txt         # Dependencies
└── assets/                  # Images and icons for README
    ├── demo1.png
    └── demo2.png
```

---

## **🔧 Installation**  
**Step 1:** Clone the repository  
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**Step 2:** Create and activate a virtual environment (Optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**Step 3:** Install dependencies  
```bash
pip install -r requirements.txt
```

**Step 4:** Download the **Face Expression Recognition Dataset** from Kaggle and place it in the project directory as follows:  
```plaintext
dataset/
└── train/
    ├── happy/
    ├── sad/
    ├── neutral/
    ├── angry/
    ├── fear/
    ├── surprise/
    └── disgust/
└── validation/
    └── ... (same structure as train)
```

---

## **⚙️ Usage**  
**Step 1:** Run the application  
```bash
python gradio_app.py
```

**Step 2:** The application will auto-launch in your default browser.  

**Step 3:** Explore the two tabs:  
- **Stylo:** Upload a **Content Image** and a **Style Image**, then click "Process" to view the **Stylized Image** and **Detected Emotion**.  
- **Grookey:** Type your query and get instant replies from the AI chatbot.  

---

## **🎨 How It Works (Workflow)**  

### **1. Neural Style Transfer (NST)**  
- Upload a **Content Image** and a **Style Image**.  
- Images are saved locally (`content.jpg` and `style.jpg`).  
- `apply_nst()` function is called, which:  
  - Loads the images.  
  - Applies style transfer using pre-trained deep learning models.  
  - Saves and returns the **Stylized Image**.  

---

### **2. Facial Expression Recognition (FER)**  
- The stylized image is passed to the `detect_emotion()` function.  
- Utilizes a **Convolutional Neural Network (CNN)** model trained on the **Face Expression Recognition Dataset**.  
- The model analyzes facial features and categorizes emotions.  
- The **Detected Emotion** is displayed as text.  

---

### **3. Grookey AI Chatbot**  
- Users interact with the chatbot by typing in the text box.  
- The input is sent to the **Grok model** using GPT4Free.  
- The model generates a response, which is appended to the **Chat History**.  
- The conversation is displayed in an interactive chat box.  
- Users can clear the conversation history anytime.  

---

## **🎥 Demo**  
### **Stylo Tab (NST & FER)**  
![NST and FER Demo](assets/demo1.png)  

### **Grookey Tab (AI Chatbot)**  
![Chatbot Demo](assets/demo2.png)  

---

## **🎯 Key Highlights**  
- **Real-Time Image Processing**: Apply NST and FER instantly.  
- **Emotional Analysis**: Detects emotions from stylized images.  
- **Conversational AI**: Grookey chatbot for interactive dialogues.  
- **Intuitive UI**: User-friendly Gradio interface with custom CSS styling.  

---

## **🌐 Deployment and Sharing**  
- Hosted locally with auto-launch feature using `webbrowser`.  
- Option to share via a public Gradio URL.  

---

## **🛠️ Future Enhancements**  
- Expand emotion categories with a more comprehensive dataset.  
- Enhance the chatbot's contextual awareness and memory.  
- Add real-time camera input for live NST and FER.  
- Implement advanced style transfer techniques like **AdaIN**.  

---

## **🤝 Contributing**  
We welcome contributions! Please follow the standard GitHub flow:  
- Fork the repository.  
- Create a new branch (`feature/new-feature`).  
- Make your changes and commit.  
- Push to the branch and submit a **Pull Request**.  

---

## **📄 License**  
This project is licensed under the **GNU GENERAL PUBLIC LICENSE** - see the [LICENSE](LICENSE) file for details.  

---

## **🎉 Acknowledgments**  
Special thanks to:  
- **GPT4Free** for the conversational AI.  
- **Gradio** for the interactive UI.  
- **Kaggle** for the Face Expression Recognition Dataset.  

---

## **🌟 Give a Star!**  
If you found this project helpful or interesting, please give it a ⭐ on GitHub!  

---

## **🚀 Get Started Now!**  
Clone the repository and explore the fusion of **Art, Emotion, and AI Conversation** like never before!  

---

## Acknowledgements
Special thanks to the open-source NLP and deep learning communities for providing the foundational tools and research that make this project possible.

