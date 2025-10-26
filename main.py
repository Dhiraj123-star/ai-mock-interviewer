import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Define interviewer agent
interviewer = Agent(
    role="Interviewer",
    goal="Conduct a technical mock interview",
    backstory="You are an experienced software engineer interviewing candidates.",
    model="gpt-4o-mini"
)

# Define task (added expected_output)
task = Task(
    description="Ask 5 technical questions about Python and provide feedback after each answer.",
    expected_output="A structured interview transcript with questions and feedback.",
    agent=interviewer
)

# Run the interview
crew = Crew(agents=[interviewer], tasks=[task])
print(crew.kickoff())
