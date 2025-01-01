from phi.agent import Agent
from phi.model.openai import OpenAIChat

# Define a new task related to Math, Logic, and Computer Science
task = (
    "Design a binary search algorithm that finds the position of a target number in a sorted list of integers. "
    "If the number is not present, return -1. Provide the algorithm as Python code, explain the step-by-step logic, "
    "and include a complexity analysis for time and space. Show the pseudocode and implementation."
)

# Create an agent for solving the task
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning=True,
    markdown=True,
    structured_outputs=True,
)

# Task execution
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)