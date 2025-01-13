from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")

#websearch Agent
websearchAgent = Agent(
    name = "Web search Agent",
    role = "Search the web for information",
    model = Groq(id="llama-3.1-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tools_calls=True,
    markdown = True,
)

#financial Agent
financialAgent = Agent(
    name = "Financial Agent",
    role = "Get financial data",
    model = Groq(id="llama-3.1-70b-versatile"),
    tools = [YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions = ["use tables to dispaly the data"],
    show_tools_calls=True,
    markdown = True,
)

multiAiAgent = Agent(
    team = [websearchAgent, financialAgent],
    model = Groq(id="llama-3.1-70b-versatile"),
    instructions = ["always include source","use tables to display data"],
    show_tools_calls=True,
    markdown = True,
)

multiAiAgent.print_response("Summarize analyst recommendations and share the latest news for NVDA",stream=True)