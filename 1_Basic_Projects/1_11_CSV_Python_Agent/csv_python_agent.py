from phi.agent.python import PythonAgent
from phi.model.openai import OpenAIChat
from phi.file.local.csv import CsvFile

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

python_agent = PythonAgent(
    model=OpenAIChat(id="gpt-4o-mini"),
    files=[
        CsvFile(
            path="https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
            description="Contains information about movies from IMDB.",
        )
    ],
    markdown=True,
    pip_install=True,
    show_tool_calls=True,
    monitoring=True,
    debug_mode=True
)

python_agent.print_response("What is the average rating of movies?")