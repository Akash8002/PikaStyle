# Import necessary libraries
import gradio as gr
from g4f.client import Client
from g4f.Provider import DeepInfra
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the G4F client with DeepInfra provider and your API key
client = Client(
    provider=DeepInfra,
    api_key="cSkAd8lAAE8jnWDL89YNMz2vaL2EPKqz"  # Your DeepInfra API key
)

# Store conversation history
chat_history = []

# Define the chatbot function
def chatbot_response(user_input):
    global chat_history
    # Add user input to chat history
    chat_history.append({"role": "user", "content": user_input})
    
    # Limit chat history to avoid rate limits
    if len(chat_history) > 10:
        chat_history = chat_history[-10:]
    
    try:
        logger.info("Sending request to DeepInfra for model: meta-llama/Meta-Llama-3.1-8B-Instruct")
        # Get response from Meta-Llama-3.1-8B-Instruct via DeepInfra
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct",  # Updated model name
            messages=chat_history  # Send full history for context
        )
        # Extract response content
        bot_reply = response.choices[0].message.content
        logger.info("Received response successfully")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        bot_reply = f"Error: {str(e)}"
    
    # Add bot reply to chat history
    chat_history.append({"role": "assistant", "content": bot_reply})
    
    # Return the chat history directly for Gradio chatbot
    return chat_history, ""

# Define clear history function
def clear_history():
    global chat_history
    chat_history = []
    return [], ""

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
    
    chatbot = gr.Chatbot(elem_classes="chatbox", type="messages")
    with gr.Row():
        msg = gr.Textbox(show_label=False, placeholder="Ask me anything...", elem_classes="input-box")
        clear = gr.Button("Clear", elem_classes="clear-button")
    
    msg.submit(chatbot_response, msg, [chatbot, msg])  # Auto-clear input box
    clear.click(clear_history, None, [chatbot, msg], queue=False)

# Launch Gradio UI
if __name__ == "__main__":
    demo.launch()