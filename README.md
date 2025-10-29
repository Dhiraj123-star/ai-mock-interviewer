# 🤖 AI Mock Interviewer

A lightweight **AI-powered mock interviewer** built using **OpenAI** and **Streamlit**.
It conducts **personalized, interactive interviews** based on **topic**, **difficulty level**, and **experience**, asking questions **one at a time**, evaluating your response, and now also:

✅ Shows the **correct / ideal answer**
✅ Explains using **real-life analogies**
✅ Allows the **candidate to ask follow-up questions** to the interviewer

---

## 🚀 Features

| Feature                               | Description                                      |
| ------------------------------------- | ------------------------------------------------ |
| 🎙️ **Live Interactive Interview**    | One question at a time, like a real interview    |
| 🎯 **Personalized Questioning**       | Tailored by topic, difficulty & experience level |
| 🧠 **Detailed Answer Evaluation**     | Strengths, weaknesses & score out of 10          |
| ✅ **Correct / Ideal Answer Provided** | Teaches the proper response                      |
| 🌱 **Analogy-Based Explanation**      | Makes complex concepts easy to understand        |
| ❓ **Candidate Follow-up Questions**   | Ask the interviewer for clarification anytime    |
| 🖥️ **Streamlit Front-End**           | Smooth, simple, and responsive UI                |
| 📜 **Downloadable Transcript**        | Full Q&A + Feedback saved for review             |

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

## 🧩 Core Flow

1. User selects:

   * 🎯 Topic
   * 🔥 Difficulty level
   * 👨‍💻 Experience level
   * #️⃣ Number of interview questions

2. AI asks the first question.

3. User responds.

4. AI provides:

   * 🧠 Feedback (Strengths / Improvements / Score)
   * ✅ Correct answer explained simply
   * 🌱 Real-life analogy for understanding

5. User may optionally ask a **follow-up question** for clarification.

6. The interview continues question-by-question until completed.

7. User can **download the full transcript**.

---

## 🧠 Example Interaction

```
Question: What is a Python decorator?

Your Answer: ...
  
🧠 Feedback:
- Good understanding of function behavior
- Missed explanation of wrapper functions
- Score: 7/10

✅ Ideal Answer:
A decorator modifies another function's behavior without changing its code...

🌱 Real-Life Analogy:
Think of wrapping a gift: the inside item stays the same, but the packaging adds something new.

❓ Follow-up Question:
"What happens to the original function metadata?"
→ AI explains clearly.
```

---

## 📄 License

MIT License

---

