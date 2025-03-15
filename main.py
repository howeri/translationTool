from pynput import keyboard
import pyperclip
from openai import OpenAI
import time

key = "enterOpenAIkey"

# Function to send text to OpenAI and get the translation
def translate_to_english(text):
    client = OpenAI(api_key=key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Just translate this into English: " + text,
            }
        ],
        model="gpt-4o",
)
    assistant_response = chat_completion.choices[0].message.content
    return assistant_response

# Function to simulate copy, translate, and paste
def translate_clipboard():
    print('test')
    # Simulate a copy (Command+C)
    controller = keyboard.Controller()
    controller.press(keyboard.Key.cmd)
    controller.press('c')
    controller.release('c')
    controller.release(keyboard.Key.cmd)

    # Wait a moment for clipboard to update
    time.sleep(0.5)

    # Get the copied text
    highlighted_text = pyperclip.paste().strip()
    if not highlighted_text:
        print("No text highlighted.")
        return

    print(f"Original text: {highlighted_text}")

    # Translate the text
    translated_text = translate_to_english(highlighted_text)
    print(f"Translated text: {translated_text}")

    # Copy the translated text to clipboard
    pyperclip.copy(translated_text)

    # Simulate a paste (Command+V)
    controller = keyboard.Controller()
    controller.press(keyboard.Key.cmd)
    controller.press('v')
    controller.release('v')
    controller.release(keyboard.Key.cmd)

    print("Translation completed and pasted.")

# Global hotkey listener
def on_activate():
    print("Hotkey triggered. Translating...")
    translate_clipboard()

# Main entry point to listen for hotkey
if __name__ == "__main__":
    # translate_to_english('111年度稅後其他綜合損益')
    hotkey = keyboard.GlobalHotKeys({'<ctrl>+<shift>+a': on_activate})
    print("Select text and press 'Ctrl+Shift+a' to paste translated text...")
    with hotkey:
        hotkey.join()  # Keep the listener running
