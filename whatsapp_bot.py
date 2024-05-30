import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import openai


openai.api_key = os.getenv('OPENAI_API_KEY')

if openai.api_key is None:
    print("Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    exit(1)

def find_chat(driver, chat_name):
    attempts = 5
    for attempt in range(attempts):
        try:
            print(f"Attempt {attempt + 1}: Searching for chat: {chat_name}")
            chat = driver.find_element(By.XPATH, f'//span[@title="{chat_name}"]')
            chat.click()
            return True
        except Exception as e:
            print(f"Chat not found. Retrying... (Attempt {attempt + 1}/{attempts})")
            time.sleep(5)  # Wait before the next attempt
    return False

def read_last_message(driver, chat_name):
    try:
        if find_chat(driver, chat_name):
            time.sleep(2)
            messages = driver.find_elements(By.CSS_SELECTOR, 'div.message-in')
            if messages:
                last_message = messages[-1].find_element(By.CSS_SELECTOR, 'span.selectable-text').text
                return last_message
        return ""
    except Exception as e:
        print(f"Error reading message: {e}")
        return ""

def send_message(driver, chat_name, message):
    try:
        if find_chat(driver, chat_name):
            time.sleep(2)
            print("Finding the message input box...")
            message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            if message_box:
                print("Message input box found. Sending message...")
                message_box.click()
                message_box.send_keys(message)
                time.sleep(5)  # Short wait before sending
                message_box.send_keys(Keys.RETURN)
                print(f"Message sent to {chat_name}: {message}")
            else:
                print("Message input box not found.")
        else:
            print(f"Failed to find chat: {chat_name}")
    except Exception as e:
        print(f"Error sending message: {e}")

def generate_response(messages):
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "I'm sorry, I couldn't process that."

def main(chat_name):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://web.whatsapp.com')
    print("Please scan the QR code to log in to WhatsApp Web.")
    time.sleep(30)  # Wait for QR code scanning and chat loading

    messages = [
        {"role": "system", "content": "You are a therapist. Be empathetic, patient, and supportive."}, 
        ]

    last_message = ""
    while True:
        new_message = read_last_message(driver, chat_name)
        if new_message and new_message != last_message:
            print(f"New message from {chat_name}: {new_message}")
            messages.append({"role": "user", "content": new_message})
            response = generate_response(messages)
            print(f"Generated response: {response}")
            send_message(driver, chat_name, response)
            messages.append({"role": "assistant", "content": response})
            last_message = new_message
        time.sleep(10)  # Check for new messages every 10 seconds

if __name__ == "__main__":
    chat_name = input("Enter the chat name: ")
    main(chat_name)

