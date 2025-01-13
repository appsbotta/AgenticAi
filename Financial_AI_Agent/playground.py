import openai
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

import phi
from phi.playground import Playground,serve_playground_app

load_dotenv()

# phi.api = os.getenv("PHI_API_KEY")

#websearch Agent
websearchAgent = Agent(
    name = "Web search Agent",
    role = "Search the web for the information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tools_calls=True,
    markdown = True,
)

#financial Agent
financialAgent = Agent(
    name = "Financial AI Agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions = ["Use tables to dispaly the data"],
    show_tools_calls=True,
    markdown = True,
)

app = Playground(agents=[financialAgent,websearchAgent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)
