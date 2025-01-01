from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=["https://aiml.com/wp-content/uploads/2023/09/Annotated-Transformers-Architecture.png"],
    stream=True,
)