# Voice AI Assistant with Raspberry Pi + ChatGPT

Build a voice-powered personal assistant using OpenAI's GPT and Raspberry Pi. It listens, speaks, and automates.

## Setup
```bash
git clone https://github.com/yourusername/voice-ai-assistant-pi.git
cd voice-ai-assistant-pi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Insert your OpenAI API key
python app/main.py
```

## Features
- Voice-to-ChatGPT-to-Voice pipeline
- Executes custom automations
- Fully local + extensible

MIT License.
