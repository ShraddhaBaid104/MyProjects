from crewai import Crew
from tasks import research_task, write_task

crew = Crew(
    agents=[research_task.agent, write_task.agent],
    tasks=[research_task, write_task],
    verbose=True
)

result = crew.kickoff()

print("\nFINAL OUTPUT:\n")
print(result)
