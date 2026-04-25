from crewai import Agent

researcher = Agent(
    role="Research Analyst",
    goal="Find accurate information",
    backstory="Expert in gathering and summarizing data",
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Write clear and engaging content",
    backstory="Skilled at turning research into readable content",
    verbose=True
)
