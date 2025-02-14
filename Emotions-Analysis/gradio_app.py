import gradio as gr
import os
from apply_nst import apply_nst
from fer_analysis import detect_emotion
from g4f.client import Client
import webbrowser

# Initialize the GPT4Free client for Chatbot
client = Client()

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
    # Store conversation history
    chat_history = []
    # Add user input to chat history
    chat_history.append(("User", user_input))
    
    # Get response from Grok model
    response = client.chat.completions.create(
        model="grok-2",  # Ensure you're using the correct model name
        messages=[{"role": "user", "content": user_input}]
    )
    # Extract response content
    bot_reply = response.choices[0].message.content
    
    # Add bot reply to chat history
    chat_history.append(("Bot", bot_reply))
    
    # Return the updated chat history and clear input box
    return chat_history, ""

# Create Gradio Interface with two pages
with gr.Blocks(css="""
    body { background-color: #f5f5f5; }
    .container { max-width: 800px; margin: auto; padding: 20px; }
    .chatbox { background: white; border-radius: 20px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; }
    .chatbot-message { background: #d1e7dd; border-radius: 15px; padding: 10px 15px; margin: 5px 0; width: fit-content; max-width: 75%; }
    .user-message { background: #f8d7da; border-radius: 15px; padding: 10px 15px; margin: 5px 0; width: fit-content; max-width: 75%; align-self: flex-end; }
    .input-box { width: 100%; border-radius: 10px; border: 1px solid #ccc; padding: 10px; margin-top: 10px; }
    .clear-button { background: #6c757d; color: white; border: none; padding: 10px 15px; border-radius: 10px; cursor: pointer; }
""") as app:
    gr.Markdown("# PikaStyle)")
    
    with gr.Tab("Stylo"):
        with gr.Row():
            content_input = gr.Image(type="pil", label="Content Image")
            style_input = gr.Image(type="pil", label="Style Image")

        output_image = gr.Image(type="filepath", label="Stylized Image")
        emotion_output = gr.Textbox(label="Detected Emotion")

        gr.Button("Process").click(
            process_image, 
            inputs=[content_input, style_input], 
            outputs=[output_image, emotion_output]
        )
    
    with gr.Tab("Grookey"):
        gr.Markdown("<h2 style='text-align: center; color: #343a40;'>🤖 Grookey</h2>")
    
        chatbot = gr.Chatbot(elem_classes="chatbox")
        with gr.Row():
            msg = gr.Textbox(show_label=False, placeholder="Ask me anything...", elem_classes="input-box")
            clear = gr.Button("Clear", elem_classes="clear-button")
        
        msg.submit(chatbot_response, msg, [chatbot, msg])  # Auto-clear input box
        clear.click(lambda: None, None, chatbot, queue=False)

# Launch Gradio App
if __name__ == "__main__":
    port = 7860  # You can change this port if needed
    url = f"http://127.0.0.1:{port}"
    webbrowser.open(url)
    app.launch(share=True, server_port=port)
