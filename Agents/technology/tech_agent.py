from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput, search_web

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TECH_PROMPT = '''
You are the Technology Research Agent. Your expertise is in emerging technologies, industry trends, and technical analysis.

When invoked, autonomously use the search_web tool to find tech articles, whitepapers, and reports.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise technology overview, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''

agent = Agent(
    name="TechnologyAgent",
    instructions=TECH_PROMPT,
    model=OpenAIChatCompletionsModel(
    model="gpt-4o",
    openai_client=client
    ),
    tools=[search_web],
    output_type=SpecialistOutput
)