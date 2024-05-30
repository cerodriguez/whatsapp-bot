# WhatsApp ChatGPT Bot

This project sets up a WhatsApp bot that uses OpenAI's GPT-4 to chat with users. The bot reads messages from a specified chat, generates responses using GPT-4, and sends those responses back to the chat. The bot is designed to maintain the context of the conversation, making the interactions feel natural and human-like.(WIP, still not working well via API)

## Prerequisites

- Python 3.7 or higher
- Google Chrome
- ChromeDriver
- OpenAI API key

## Installation

1. **Clone the repository**:
    ```bash
    git clone git@github.com:cerodriguez/whatsapp-bot.git
    cd whatsapp-bot
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key**:
    - On macOS/Linux:
      ```bash
      export OPENAI_API_KEY=your_openai_api_key
      ```

## Configuration

1. **Update the system message**:
    - You can customize the system message to set the behavior and tone of the AI. This message helps the AI understand how it should respond in the conversation.

    ```python
    messages = [{"role": "system", "content": "Talk like a real person, use slang, be casual and engaging. Respond naturally like you're chatting with a friend. Avoid sounding like a bot or assistant."}]
    ```

## Usage

1. **Run the script**:
    ```bash
    python3 whatsapp_bot.py
    ```

2. **Enter the chat name**:
    - When prompted, enter the exact name of the chat as it appears in WhatsApp Web.

3. **Scan the QR code**:
    - Open WhatsApp Web and scan the QR code to log in.

4. **Interact with the bot**:
    - The bot will read messages from the specified chat, generate responses using GPT-4, and send those responses back to the chat.

