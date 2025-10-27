
# 🤖 AI Mock Interviewer

A lightweight **AI-powered mock interviewer** built using **CrewAI**, **OpenAI**, and **Streamlit**.
It conducts **personalized, interactive interviews** based on **topic**, **difficulty level**, and **experience**, asking one question at a time and providing **real-time feedback**.

---

## 🚀 Features

* 💬 Conducts live **interactive interviews** — one question at a time
* 🧠 Uses **CrewAI** for orchestrating intelligent agents:

  * **Question Generator** — crafts tailored technical questions
  * **Answer Evaluator** — evaluates your responses and gives feedback
  * **Interviewer Agent** — manages the flow of the interview
* 🎯 Customizable by **topic**, **difficulty level**, and **experience level**
* 🖥️ Interactive **Streamlit UI** for seamless experience
* 📜 Structured **question-answer-feedback transcript**
* 💾 Option to **download the interview transcript** after completion

---

## ⚙️ Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Add your OpenAI API key** to `.env`

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run main.py
   ```

---

## 🧩 Core Functionality

* Prompts user for:

  * 🎯 **Interview topic**
  * 🧩 **Difficulty level** (Beginner / Intermediate / Advanced)
  * 👨‍💻 **Experience level** (Fresher / Mid-level / Senior)
* Dynamically generates technical questions using the **Question Generator Agent**
* Collects user responses and evaluates them with the **Answer Evaluator Agent**
* Displays live results and feedback interactively in Streamlit
* Saves a structured transcript that can be downloaded for review

---

## 🧠 Example Flow

1. User selects:

   * Topic: *System Design*
   * Difficulty: *Advanced*
   * Experience: *Senior*
2. AI asks the first question.
3. User answers.
4. AI evaluates and gives feedback.
5. AI proceeds to the next question — until the interview ends.
6. User downloads the complete transcript.

---

## 📄 License

MIT License

---

