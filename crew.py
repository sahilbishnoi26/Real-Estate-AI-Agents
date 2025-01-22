from crewai import Crew  # Import the Crew class to manage agents and tasks
from agents import property_researcher, property_analyst  # Import predefined agents
from tasks import research_task, analysis_task  # Import predefined tasks

# Create a Crew instance to manage the agents and their tasks
crew = Crew(
    agents=[property_researcher, property_analyst],  # Assign the agents to the crew
    tasks=[research_task, analysis_task],  # Assign the tasks to be executed
    verbose=True  # Enable detailed logging for debugging and insights
)

# Execute the tasks using the crew's agents
task_output = crew.kickoff()  # Starts the task execution and collects the output

# Print the results of the task execution
print(task_output)  # Outputs the final result for review
