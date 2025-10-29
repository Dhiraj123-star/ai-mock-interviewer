import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    st.error("❌ OPENAI_API_KEY not found in environment. Please add it to .env file.")
    st.stop()

client = OpenAI(api_key=openai_key)

# Streamlit setup
st.set_page_config(page_title="🤖 AI Mock Interviewer", page_icon="🧠", layout="centered")
st.title("🤖 AI Mock Interviewer")
st.markdown("An **AI-powered live mock interviewer** tailored to your topic, experience, and difficulty level.")

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False
if "interview_over" not in st.session_state:
    st.session_state.interview_over = False
if "transcript" not in st.session_state:
    st.session_state.transcript = ""
if "question_count" not in st.session_state:
    st.session_state.question_count = 0

# 🧠 Collect User Preferences
st.sidebar.header("⚙️ Interview Settings")
topic = st.sidebar.text_input("🎯 Interview Topic:", "Python")
experience_level = st.sidebar.selectbox("💼 Experience Level:", ["Beginner", "Intermediate", "Expert"])
difficulty = st.sidebar.selectbox("🔥 Question Difficulty:", ["Easy", "Medium", "Hard"])
total_questions = st.sidebar.number_input("🧩 Number of Questions:", min_value=1, max_value=10, value=5, step=1)

# 🧩 Generate question dynamically
def generate_question(topic, exp_level, difficulty, prev_qs):
    prompt = (
        f"You are an expert interviewer conducting a {difficulty.lower()} interview "
        f"for a {exp_level.lower()} candidate on {topic}.\n"
        f"Previous questions asked: {prev_qs}\n"
        f"Ask the next question.\nReturn only the question text without explanation."
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()

# 🧩 Evaluate answer
def evaluate_answer(question, answer, exp_level):
    prompt = (
        f"You are a senior interviewer assessing a {exp_level.lower()} candidate.\n\n"
        f"Interview Question: {question}\n"
        f"Candidate Answer: {answer}\n\n"
        "Your evaluation should be structured and easy to follow.\n"
        "Provide the response in this format:\n\n"
        "### 🧠 Feedback\n"
        "- What the candidate did well\n"
        "- What needs improvement\n"
        "- Score (x/10)\n\n"
        "### ✅ Correct / Ideal Answer (Explain Simply)\n"
        "- Provide a clear, concise, and correct answer.\n"
        "- Rewrite it in beginner-friendly language.\n\n"
        "### 🌱 Real-Life Analogy\n"
        "- Explain the concept using a real-world analogy or metaphor.\n"
        "- Keep the analogy short but effective.\n"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


# 🎯 Start Interview
if st.button("🚀 Start Personalized Interview"):
    intro_prompt = (
        f"You are an interviewer about to start a mock interview.\n"
        f"Topic: {topic}, Candidate Level: {experience_level}, Difficulty: {difficulty}.\n"
        f"Introduce yourself and explain how the interview will work in 2-3 sentences."
    )
    intro_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": intro_prompt}]
    )
    st.markdown(f"### 👋 Introduction\n{intro_response.choices[0].message.content.strip()}")
    
    st.session_state.current_question = generate_question(topic, experience_level, difficulty, [])
    st.session_state.answer_submitted = False
    st.session_state.interview_over = False
    st.session_state.transcript = ""
    st.session_state.question_count = 1

# 💬 Show question
if st.session_state.current_question and not st.session_state.interview_over:
    st.subheader(f"Question {st.session_state.question_count}")
    st.markdown(f"**{st.session_state.current_question}**")

    answer = st.text_area("💬 Your Answer:", key=f"answer_{st.session_state.question_count}")

    if st.button("Submit Answer"):
        if answer.strip():
            feedback = evaluate_answer(st.session_state.current_question, answer, experience_level)

            st.session_state.transcript += (
                f"Question {st.session_state.question_count}: {st.session_state.current_question}\n\n"
                f"Answer: {answer}\n\n"
                f"Feedback:\n{feedback}\n\n---\n\n"
            )

            st.markdown("### 🧠 Interviewer Feedback")
            st.write(feedback)

            st.session_state.question_count += 1
            if st.session_state.question_count <= total_questions:
                st.session_state.current_question = generate_question(
                    topic, experience_level, difficulty, st.session_state.transcript
                )
            else:
                st.session_state.interview_over = True

# 🏁 End of Interview
if st.session_state.interview_over:
    st.success("🎉 Interview Completed!")
    st.markdown("### 📜 Full Interview Transcript")
    st.code(st.session_state.transcript)
    st.download_button(
        "📄 Download Interview Transcript",
        st.session_state.transcript,
        file_name=f"{topic.lower()}_interview_transcript.txt",
    )
