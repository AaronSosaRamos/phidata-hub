from phi.agent import Agent
from phi.model.openai import OpenAIChat

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

agent = Agent(model=OpenAIChat(id="gpt-4o-mini"), markdown=True, monitoring=True, debug_mode=True)
agent.print_response("Share a 2 sentence about the Qucksort algorithm using the Feynman technique.", stream=True)