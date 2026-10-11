# Sahayak — Multilingual Voice Agent for Bharat

Built by **Mrinmoy Mondal** using Sarvam AI.

## 🌍 The Problem

Over 700 million Indians speak regional languages and naturally mix English into their speech (Hinglish, Tanglish). Existing voice assistants like Siri, Alexa, and Google Assistant fail on this code-mixed, disfluent, real-world speech — locking rural users out of government schemes and financial services.

## 💡 The Solution

Sahayak is a voice-first AI agent that:
- Understands code-mixed Indian speech using Sarvam Saaras v3 (codemix mode)
- Reasons about user intent using Sarvam-105B
- Responds in the user's own language using Sarvam Bulbul v3

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Speech-to-Text | Sarvam Saaras v3 (codemix mode) |
| Reasoning | Sarvam-105B |
| Text-to-Speech | Sarvam Bulbul v3 (priya voice) |
| Language | Python 3.10 |
| UI | Streamlit + CLI |
| SDK | sarvamai (official Sarvam Python SDK) |

## 🚀 Setup

1. Clone the repo:
   git clone https://github.com/mrinmaxx/sahayak-sarvam.git
   cd sahayak-sarvam

2. Install dependencies:
   pip install -r requirements.txt

3. Create a .env file with your Sarvam API key:
   SARVAM_API_KEY=your_key_here

4. Run the CLI demo:
   python cli_app.py

5. (Optional) Run the Streamlit UI:
   streamlit run ui/app.py

## 🎬 Demo

Run python cli_app.py and try:
- Language: hi-IN
- Mode: text
- Question: PM kisan ka paisa aaya ki nahi?

You will get a Hindi voice response saved to data/cache/response.wav

## 🏗️ Architecture

User voice -> Sarvam Saaras STT (codemix) -> Sarvam-105B -> Sarvam Bulbul TTS -> Audio response

## 👤 Author

**Mrinmoy Mondal**
