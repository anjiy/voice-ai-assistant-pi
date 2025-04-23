# Voice AI Assistant on Raspberry Pi

A smart voice assistant powered by ChatGPT, running on a Raspberry Pi. It can listen, respond intelligently, and even trigger home automation tasks.

---

## 🧠 Features
- 🎙️ Speech-to-Text using `speech_recognition`
- 🗣️ Text-to-Speech using `gTTS`
- 🤖 ChatGPT integration via OpenAI API
- ⚡ Simple Home Automation Trigger (mock example)
- 🔊 Plays responses with `playsound`
- 🎛️ Easy to customize and extend

---

## 🏗️ Folder Structure
```
voice-ai-assistant-pi/
│
├── assistant/               # Core assistant logic
│   ├── __init__.py
│   ├── config.py            # Environment config loader
│   ├── recognizer.py        # Speech recognition
│   ├── speaker.py           # TTS engine
│   ├── chatgpt.py           # ChatGPT API wrapper
│   └── automation.py        # Triggering home automations
│
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
├── .env.example             # API key environment example
├── README.md                # Project documentation
└── LICENSE                  # MIT License
```

---

## 🚀 How to Run

1. **Clone the repo:**
```bash
git clone https://github.com/yourusername/voice-ai-assistant-pi.git
cd voice-ai-assistant-pi
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Add your OpenAI key:**
Rename `.env.example` → `.env` and update:
```env
OPENAI_API_KEY=your-key-here
```

4. **Run the app:**
```bash
python main.py
```

---

## 🔐 Environment Variables
Make sure you set the following in your `.env` file:
- `OPENAI_API_KEY`

---

## 📝 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🌱 Future Ideas
- Voice command dashboard (Flask or React)
- Smart device integration (e.g., lights, fans)
- Multi-language support
- Wake word detection ("Hey Pi")

---

Feel free to fork, contribute, and build your own voice assistant! ✨

---

### 💬 Let's Collaborate
If you’re working on voice tech, AI apps, or Raspberry Pi projects — reach out! Would love to exchange ideas.

---
