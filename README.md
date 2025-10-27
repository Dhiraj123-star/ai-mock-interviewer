
# 🤖 AI Mock Interviewer

A lightweight **AI-powered mock interviewer** built using **CrewAI**, **OpenAI**, and **Streamlit**.
It conducts a **technical interview**, provides **feedback for each response**, and displays everything in a **clean, user-friendly web interface**.

---

## 🚀 Features

* 💬 Conducts mock interviews using OpenAI’s GPT model
* 🧠 Uses CrewAI for intelligent agent orchestration
* 🖥️ Interactive **Streamlit web UI** for easy use
* 📜 Clean **Markdown-formatted transcript** with questions, answers, and feedback
* 💾 Option to **download interview transcript** after completion

---

## ⚙️ Setup

1. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

2. Add your OpenAI API key in `.env`

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

3. Run the app

   ```bash
   streamlit run main.py
   ```

---

## 🧩 Core Functionality

* Initializes a **CrewAI agent** as an interviewer
* Uses **OpenAI GPT model** to generate and evaluate interview content
* Displays a **beautifully formatted transcript** via Streamlit
* Allows **real-time streaming** and **easy transcript download**

---

## 📄 License

MIT License
