
# 🤖 AI Mock Interviewer

A lightweight **AI-powered mock interviewer** built using **OpenAI** and **Streamlit**.
It conducts **personalized interviews** based on topic, difficulty, and experience — asking **one question at a time**, evaluating your answer, and helping you improve with clear, structured feedback.

Now includes:

✅ **Correct/Ideal Answers**
✅ **Real-Life Analogies**
✅ **Candidate Follow-Up Questions**
🎙️ **Voice Answer Input (Speech → Text)**
🔊 **AI Spoken Feedback (Text → Speech)**

---

## 🚀 Features Overview

| Feature                     | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| 💬 Live Q&A Interview       | One question at a time, like a real job interview     |
| 🎯 Personalized Questioning | Based on topic, experience, and difficulty level      |
| 🧠 Smart Evaluation         | Highlights strengths, weaknesses, and gives a score   |
| ✅ Ideal Answer Provided     | Learn how you *should* answer in real interviews      |
| 🌱 Real-Life Analogy        | Simplifies difficult concepts using everyday examples |
| ❓ Ask Follow-Up Questions   | Candidate can ask interviewer for clarification       |
| 🎙️ **Speech Input**        | Answer using your **voice**, powered by **Whisper**   |
| 🔊 **Speech Output**        | Interviewer feedback is spoken aloud using **TTS**    |
| 📥 Transcript Download      | Save the entire interview for later review            |

---

## 🎙️ Voice Features (New)

| Feature           | Description                                 | Model Used        |
| ----------------- | ------------------------------------------- | ----------------- |
| **Speech → Text** | Converts your recorded voice answer to text | `whisper-1`       |
| **Text → Speech** | AI reads feedback aloud in natural voice    | `gpt-4o-mini-tts` |

This allows a **hands-free interview experience** — speak answers and listen to feedback like a real conversation.

---

## ⚙️ Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Add your OpenAI API Key** in `.env`

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

3. **Run the application**

   ```bash
   streamlit run main.py
   ```

---

## 🧩 Interview Flow

1. Choose:

   * Topic
   * Difficulty level
   * Experience level
   * Number of questions

2. AI interviewer asks a question

3. You reply:

   * 📝 by typing **or**
   * 🎙️ by recording your voice

4. AI evaluates and responds with:

   * 🧠 Feedback
   * ✅ Ideal Answer
   * 🌱 Analogy
   * 🔊 Spoken audio feedback

5. You can ask follow-up questions

6. Continue until interview completes

7. Download full transcript

---

## 🧠 Sample Interaction

```
Question: What is Dependency Injection?

Your Answer: (spoken or typed)

🧠 Feedback:
- Good start explaining the concept.
- Missing mention of inversion of control.
- Score: 6/10

✅ Ideal Answer:
Dependency Injection is a design pattern where objects receive their dependencies externally...

🌱 Analogy:
Think of plugging a charger into a phone — the phone doesn't create electricity...

🔊 Spoken Feedback:
AI reads the above aloud.
```

---

## 📄 License

MIT License

---
