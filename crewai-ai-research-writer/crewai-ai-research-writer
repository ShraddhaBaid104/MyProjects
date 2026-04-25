from crewai import Task
from agents import researcher, writer

research_task = Task(
    description="Research about AI agents and their use cases",
    expected_output="A detailed summary of AI agents and their real-world applications",
    agent=researcher
)

write_task = Task(
    description="Write a blog post based on the research",
    expected_output="A well-structured blog post explaining AI agents in simple terms",
    agent=writer
)
