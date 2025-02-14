# Import necessary libraries
import gradio as gr
from g4f.client import Client

# Initialize the G4F client
client = Client()

# Store conversation history
chat_history = []

# Define the chatbot function
def chatbot_response(user_input):
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

# Gradio UI
with gr.Blocks(css="""
    body { background-color: #f5f5f5; }
    .container { max-width: 800px; margin: auto; padding: 20px; }
    .chatbox { background: white; border-radius: 20px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; }
    .chatbot-message { background: #d1e7dd; border-radius: 15px; padding: 10px 15px; margin: 5px 0; width: fit-content; max-width: 75%; }
    .user-message { background: #f8d7da; border-radius: 15px; padding: 10px 15px; margin: 5px 0; width: fit-content; max-width: 75%; align-self: flex-end; }
    .input-box { width: 100%; border-radius: 10px; border: 1px solid #ccc; padding: 10px; margin-top: 10px; }
    .clear-button { background: #6c757d; color: white; border: none; padding: 10px 15px; border-radius: 10px; cursor: pointer; }
""") as demo:
    gr.Markdown("<h2 style='text-align: center; color: #343a40;'>🤖 Grookey</h2>")
    
    chatbot = gr.Chatbot(elem_classes="chatbox")
    with gr.Row():
        msg = gr.Textbox(show_label=False, placeholder="Ask me anything...", elem_classes="input-box")
        clear = gr.Button("Clear", elem_classes="clear-button")
    
    msg.submit(chatbot_response, msg, [chatbot, msg])  # Auto-clear input box
    clear.click(lambda: None, None, chatbot, queue=False)

# Launch Gradio UI
if __name__ == "__main__":
    demo.launch(share=True)
