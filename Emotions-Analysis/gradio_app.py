# Import necessary libraries
import gradio as gr
import os
from apply_nst import apply_nst
from fer_analysis import detect_emotion
from g4f.client import Client
from g4f.Provider import DeepInfra
import webbrowser
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the G4F client with DeepInfra provider and your API key
client = Client(
    provider=DeepInfra,
    api_key="cSkAd8lAAE8jnWDL89YNMz2vaL2EPKqz"  # Replace with your actual API key
)

# Store conversation history
chat_history = []

# Define Paths for NST and FER
content_image_path = "content.jpg"
style_image_path = "style.jpg"
output_image_path = "stylized_output.jpg"

# Function for NST and FER
def process_image(content, style):
    content.save(content_image_path)
    style.save(style_image_path)

    # Apply Neural Style Transfer (NST)
    stylized_path = apply_nst(content_image_path, style_image_path, output_image_path)

    # Perform Facial Expression Recognition (FER)
    emotion = detect_emotion(stylized_path)

    return stylized_path, emotion

# Define the chatbot function
def chatbot_response(user_input):
    global chat_history
    chat_history.append({"role": "user", "content": user_input})

    if len(chat_history) > 10:
        chat_history = chat_history[-10:]

    try:
        logger.info("Sending request to DeepInfra for model: meta-llama/Meta-Llama-3.1-8B-Instruct")
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct",
            messages=chat_history
        )
        bot_reply = response.choices[0].message.content
        logger.info("Received response successfully")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        bot_reply = f"Error: {str(e)}"

    chat_history.append({"role": "assistant", "content": bot_reply})
    return chat_history, ""

def clear_history():
    global chat_history
    chat_history = []
    return [], ""

# Gradio Interface with Emoji-based Visual Cues
with gr.Blocks(css="""
    body { background-color: #f5f5f5; }
    .container { max-width: 800px; margin: auto; padding: 20px; }
    .chatbox { background: white; border-radius: 20px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; }
    .chatbot-message { background: #d1e7dd; border-radius: 15px; padding: 10px 15px; margin: 5px 0; width: fit-content; max-width: 75%; }
    .user-message { background: #f8d7da; border-radius: 15px; padding: 10px 15px; margin: 5px 0; width: fit-content; max-width: 75%; align-self: flex-end; }
    .input-box { width: 100%; border-radius: 10px; border: 1px solid #ccc; padding: 10px; margin-top: 10px; }
    .clear-button { background: #6c757d; color: white; border: none; padding: 10px 15px; border-radius: 10px; cursor: pointer; }
""") as app:
    gr.Markdown("# 🎨 PikaStyle")

    with gr.Tab("🖼️ Stylo - Neural Style Transfer"):
        with gr.Row():
            content_input = gr.Image(type="pil", label="🧠 Content Image")
            style_input = gr.Image(type="pil", label="🎭 Style Image")

        output_image = gr.Image(type="filepath", label="🖌️ Stylized Output")
        emotion_output = gr.Textbox(label="🧠 Detected Emotion")

        gr.Button("✨ Process", elem_id="process-btn").click(
            process_image,
            inputs=[content_input, style_input],
            outputs=[output_image, emotion_output]
        )

    with gr.Tab("💬 Grookey - AI Chatbot"):
        gr.Markdown("<h2 style='text-align: center; color: #343a40;'>🤖 Grookey Chat Assistant</h2>")

        chatbot = gr.Chatbot(elem_classes="chatbox", type="messages")
        with gr.Row():
            msg = gr.Textbox(show_label=False, placeholder="Ask Grookey something cool...", elem_classes="input-box")
            clear = gr.Button("🧹 Clear Chat", elem_classes="clear-button")

        msg.submit(chatbot_response, msg, [chatbot, msg])
        clear.click(clear_history, None, [chatbot, msg], queue=False)

# Launch Gradio App
if __name__ == "__main__":
    port = 7860
    url = f"http://127.0.0.1:{port}"
    webbrowser.open(url)
    app.launch(server_port=port)
