import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Streamlit setup
st.set_page_config(page_title="🤖 AI Mock Interviewer", page_icon="🧠", layout="centered")
st.title("🤖 AI Mock Interviewer")
st.markdown("Prepare for your next interview with an **AI-powered mock interviewer**!")

# User input
topic = st.text_input("🎯 Enter interview topic (e.g., Python, Django, System Design):", "Python")

if st.button("Start Interview"):
    st.info("🚀 Interview is starting... please wait.")
    with st.spinner("AI is generating questions and feedback..."):
        # Define interviewer agent
        interviewer = Agent(
            role="Interviewer",
            goal=f"Conduct a technical mock interview on {topic}.",
            backstory="You are an experienced senior engineer interviewing candidates.",
            model="gpt-4o-mini"
        )

        # Define the interview task
        task = Task(
            description=f"Ask 5 technical questions about {topic} and provide feedback after each answer.",
            expected_output="A conversational, markdown-friendly transcript with questions, answers, and feedback.",
            agent=interviewer
        )

        placeholder = st.empty()

        def stream_output():
            # Run Crew and return a cleaned transcript string
            crew = Crew(agents=[interviewer], tasks=[task])
            result = crew.kickoff()

            # result may be a dict-like object from CrewAI; prefer "raw" if present
            if isinstance(result, dict):
                # try common fields
                for key in ("raw", "output", "transcript"):
                    if key in result and result[key]:
                        return str(result[key])
                return str(result)
            return str(result)

        # Call the streamer and update UI
        full_output = stream_output()
        # Replace escaped newline sequences if present
        formatted = full_output.replace("\\n", "\n")
        placeholder.markdown(formatted)

    st.success("✅ Interview completed!")
    st.markdown("---")
    st.download_button("📄 Download Interview Transcript", formatted, file_name="interview_transcript.txt")
