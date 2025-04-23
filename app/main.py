from speech_to_text import listen_to_voice
from text_to_speech import speak
from chatgpt_handler import ask_chatgpt
from automation import execute_automation

if __name__ == '__main__':
    while True:
        query = listen_to_voice()
        if query:
            print("You said:", query)
            response = ask_chatgpt(query)
            print("Assistant:", response)
            speak(response)
            execute_automation(response)