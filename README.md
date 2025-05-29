# Gemini Multi-Turn Chatbot (Console-Based)

This is a simple, context-aware chatbot that uses Google's **Gemini API** to carry on interactive multi-turn conversations via the terminal. It maintains context across messages and allows users to set the model's temperature (creativity level).

---

## 🚀 Features

- 🧠 Maintains full conversation context across turns
- 🎛️ Supports temperature adjustment to control response creativity
- 💬 Simple console input/output (no GUI)
- 🛑 Gracefully exits with `exit` or `quit`
- 🔐 Secure API key handling via `.env` file

---


## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gemini-multi-turn-chat.git
cd gemini-multi-turn-chat

2. Install Dependencies

pip install -r requirements.txt

3. Get a Gemini API Key

1.Go to Google AI Studio and sign in.
2.Generate your API key from the API Keys section.

🔐 Setting Up the API Key
GEMINI_API_KEY=your-api-key-here
▶️ How to Run
python gemini_chat.py
