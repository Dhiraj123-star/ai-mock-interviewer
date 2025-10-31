
# 🤖 AI Mock Interviewer

A lightweight **AI-powered mock interviewer** built using **OpenAI** and **Streamlit**.
It conducts **personalized interviews** based on topic, difficulty, and experience — asking **one question at a time**, evaluating your answers, and helping you improve with clear, structured feedback.

Now includes:

✅ **Correct / Ideal Answers**
✅ **Real-Life Analogies for Understanding**
✅ **Candidate Follow-Up Questions**
🎙️ **Voice Input (Speech → Text)**
🔊 **AI Spoken Feedback (Text → Speech)**
🐳 **Docker Support**
🚀 **CI/CD Deployment to Docker Hub**

---

## 🚀 Feature Overview

| Feature                       | Description                                        |
| ----------------------------- | -------------------------------------------------- |
| 💬 Live Q&A Interview         | One realistic interview question at a time         |
| 🎯 Personalized Questioning   | Tailored by topic, difficulty & experience         |
| 🧠 Smart Evaluation           | Strengths, weaknesses, and scoring                 |
| ✅ Ideal Answer Provided       | Teaches how to respond correctly                   |
| 🌱 Real-Life Analogies        | Explains complex topics simply                     |
| ❓ Follow-Up Questions Allowed | Candidate can ask the interviewer                  |
| 🎙️ Voice Answer Input        | Use your microphone to answer using **Whisper**    |
| 🔊 Spoken AI Feedback         | AI speaks responses via **Text-to-Speech**         |
| 📥 Transcript Download        | Save full interview for review                     |
| 🐳 Docker Support             | Containerized and ready for deployment             |
| 🚀 CI/CD Auto Deploy          | Auto-build & push to Docker Hub via GitHub Actions |

---

## 🎙️ Voice Features (New)

| Feature           | Description                        | Model Used                |
| ----------------- | ---------------------------------- | ------------------------- |
| **Speech → Text** | Convert your spoken answer to text | `whisper-1`               |
| **Text → Speech** | AI speaks feedback naturally       | `gpt-4o-mini-tts` (voice) |

---

## ⚙️ Local Setup

```bash
pip install -r requirements.txt
streamlit run main.py
```

Add your **API key** inside `.env`:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 🐳 Docker Setup

### **Build the Image**

```bash
docker build -t ai-mock-interviewer .
```

### **Run the Container**

```bash
docker run -p 8501:8501 ai-mock-interviewer
```

---

## 🐳 docker-compose (Recommended)

```bash
docker-compose up --build
```

This automatically builds and serves the app at:

```
http://localhost:8501
```

---

## 🚀 CI/CD (Auto-Deploy to Docker Hub)

This project includes a **GitHub Actions Pipeline** that:

1. Builds the Docker image
2. Tags it as `latest`
3. Pushes it to **Docker Hub**
4. Runs on every push to `main`

Add the following secrets in your repo:

| Secret Name          | Value                    |
| -------------------- | ------------------------ |
| `DOCKERHUB_USERNAME` | Your Docker Hub Username |
| `DOCKERHUB_TOKEN`    | Docker Hub Access Token  |

Pipeline file:
`.github/workflows/docker-publish.yml`

---

## 🧩 Interview Flow

1. Select **topic**, **difficulty**, **experience**, and **question count**
2. AI interviewer asks a question
3. Answer via **typing or speaking**
4. AI gives:

   * 🧠 Feedback
   * ✅ Ideal Answer
   * 🌱 Analogy
   * 🔊 Spoken Feedback
5. Optionally ask a follow-up question
6. Continue until completed
7. Download transcript

---

## 📄 License

MIT License

---
