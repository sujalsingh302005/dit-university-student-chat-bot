# dit-university-student-chat-bot
AI-powered voice-enabled Mental Health Assistant for DIT University built using Python, Tkinter and locally hosted Mistral LLM via Ollama with real-time streaming responses.
# 🧠 DIT University Mental Health AI Assistant

An AI-powered **voice-enabled desktop chatbot** developed for DIT University students using a locally hosted **Mistral Large Language Model (LLM)**.

This project demonstrates real-world AI system integration by combining a local LLM, streaming responses, speech output, and a responsive desktop interface built with Python.

The assistant runs completely **offline**, ensuring privacy, fast performance, and independence from paid cloud APIs.

---

## 🚀 Project Overview

The DIT University Mental Health AI Assistant simulates an intelligent conversational companion capable of answering student queries while speaking responses aloud in real time.

The system integrates:

* Local AI inference
* Real-time response streaming
* Voice interaction
* Multithreaded desktop application design

---

## ✨ Features

* Local AI chatbot powered by **Mistral LLM**
* Voice speaking assistant (Text-to-Speech)
* Real-time streaming responses
* Clean desktop GUI using Tkinter
* Multithreaded architecture for smooth performance
* Speech queue system preventing overlapping audio
* Offline execution (No API key required)
* Privacy-focused AI interaction

---

## 🧠 AI Model

* Model Used: **Mistral**
* Runtime: **Ollama Local LLM Server**
* Inference Type: Streaming Token Generation
* Execution Mode: Fully Local

---

## 🛠️ Tech Stack

* Python
* Tkinter (GUI Development)
* Ollama
* Mistral LLM
* Requests (REST API Communication)
* Multithreading
* Queue Management
* macOS Speech Engine (`say`)

---

## 🏗️ System Architecture

User Input
↓
Tkinter GUI
↓
Python Backend
↓
REST API Request
↓
Ollama Server (localhost:11434)
↓
Mistral LLM
↓
Streaming Response
↓
Voice Output + Chat Display

---

## 📂 Project Structure

dit-university-mental-health-ai-assistant/

gui/
  chat_gui.py

screenshots/
  chatbot.png

README.md
requirements.txt
.gitignore

---

## ⚙️ Installation & Setup

### 1️⃣ Install Ollama

Download and install Ollama:

https://ollama.com

Verify installation:

ollama --version

---

### 2️⃣ Download Mistral Model

ollama pull mistral

(This is a one-time setup.)

---

### 3️⃣ Start AI Server

ollama serve

Keep this terminal running.

---

### 4️⃣ Install Python Dependencies

pip install -r requirements.txt

---

### 5️⃣ Run Application

python gui/chat_gui.py

---

## 🎙️ Voice Assistant Capability

The assistant converts AI responses into speech using a queued voice system that:

* Prevents overlapping audio
* Maintains natural conversation flow
* Provides real-time spoken interaction

---

## ⚡ Technical Highlights

* Streaming LLM response handling
* Thread-safe speech queue implementation
* Non-blocking GUI using multithreading
* Local LLM integration via REST API
* Offline conversational AI assistant

---

## 🔒 Privacy Advantage

Unlike cloud-based AI assistants:

* No API keys required
* No user data sent externally
* Fully local execution
* Secure and private conversations

---

## 📈 Future Enhancements

* Speech-to-Text input
* Conversation memory
* Emotion-aware responses
* Dark/Light UI themes
* Standalone desktop packaging

---

## 👨‍💻 Author

Sujal Singh
B.Tech CSE — DIT University
AI & Software Development Enthusiast

GitHub: https://github.com/sujalsingh302005

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
