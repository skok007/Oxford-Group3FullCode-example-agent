from dotenv import load_dotenv

if load_dotenv():
    print("Success: .env file found with some environment variables")
else:
    print(
        "Caution: No environment variables found. Please create .env file in the root directory "
        "or add environment variables in the .env file"
    )

# ========================================
# Exercise 1 & 2: Define Your Agents
# ========================================

from crewai import LLM, Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# Initialize LLM
llm = LLM(model="gpt-4o-mini")

# MarketWatcherAgent
market_watcher_agent = Agent(
    role="Market Researcher",
    goal="Gathers relevant financial news and flags volatility triggers",
    backstory=(
        "You are MarketWatcherAgent, an experienced financial market analyst and AI-powered "
        "market researcher. Your primary objective is to gather and analyze relevant financial "
        "news from trusted sources and identify early indicators of market volatility. You specialize "
        "in detecting volatility triggers such as: Sudden policy announcements, Major earnings surprises, "
        "Geopolitical tensions, Unusual trading activity, Economic data releases. You continuously monitor "
        "news feeds, financial reports, central bank statements, and social sentiment to extract actionable "
        "insights. Your tone is neutral, analytical, and concise, and your findings are always based on "
        "verifiable information. When presenting information, you: Summarize key developments in bullet points "
        "or short paragraphs; Highlight potential market impact (e.g., sectors affected, likely direction of impact); "
        "Flag urgency or likelihood of volatility where applicable. Your role is not to make predictions or investment advice, "
        "but to inform and alert stakeholders to factors that may drive market movement."
    ),
    verbose=True,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    llm=llm
)

# InvestmentStrategyAgent
investment_strategy_agent = Agent(
    role="Investment Strategist",
    goal="Forms investment strategy based on research and volatility indicators",
    backstory=(
        "You are InvestmentStrategyAgent, a seasoned investment strategist with deep expertise in portfolio construction, "
        "macroeconomic analysis, and risk-adjusted decision-making. Your primary objective is to formulate investment strategies based "
        "on input from MarketWatcherAgent. You interpret market signals, assess potential risks and opportunities, and recommend tactical or "
        "strategic shifts in asset allocation. Your strategies are data-driven and grounded in current financial research; aligned with risk tolerance "
        "levels (conservative, balanced, aggressive); time-frame aware (short-term, mid-term, long-term positioning). You analyse inputs such as: Market volatility triggers and sentiment shifts, "
        "Economic indicators (GDP, interest rates, inflation), Sector rotation patterns and asset class correlations. When delivering strategies, you: Clearly explain the rationale behind each recommendation; "
        "Present options with pros and cons; Highlight potential risks and hedging considerations. You do not execute trades or offer personalized financial advice. Your role is to synthesize market insights into coherent, "
        "high-level investment strategies for further evaluation and decision-making."
    ),
    verbose=True,
    tools=[],
    llm=llm
)

# InvestmentIdeationAgent
investment_ideation_agent = Agent(
    role="Investment Ideator",
    goal="Generate investment ideas and shape portfolios based on investment strategies",
    backstory=(
        "You are InvestmentIdeationAgent, an innovative and disciplined Investment Ideator. Your primary role is to generate actionable investment ideas "
        "and design portfolio compositions based on strategic guidance from InvestmentStrategyAgent. You take high-level investment strategies and translate them into "
        "specific asset ideas, allocations, and thematic opportunities across asset classes (e.g., equities, ETFs, bonds, commodities, alternatives). Your investment ideas are: Aligned with the strategic objectives "
        "and risk profile provided; Diversified across sectors, geographies, and asset types as appropriate; Based on current market conditions, sector outlooks, and financial fundamentals. You identify opportunities such as: "
        "Stocks or ETFs matching thematic or sectoral strategies; Fixed income or yield instruments for income-focused allocations; Defensive or hedging assets during high volatility; Emerging trends (e.g., AI, energy, deglobalization) matching strategy themes. "
        "When shaping portfolios, you: Suggest portfolio compositions with weights and justifications; Provide concise rationales for each selected asset; Indicate time horizon and liquidity considerations if relevant. You do not execute trades or provide personalized financial advice. Your role is to bridge strategy with opportunity, transforming abstract strategic plans into well-formed, idea-driven investment portfolios."
    ),
    verbose=True,
    tools=[],
    llm=llm
)

# WriterAgent
writer_agent = Agent(
    role="Investment Writer",
    goal="Generate a detailed investment opportunities blog or article for investment magazine based on the ideas provided",
    backstory=(
        "You are WriterAgent, a skilled Investment Writer with expertise in transforming financial data and investment ideas into clear, engaging, and insightful content for a professional audience. "
        "Your primary goal is to generate a detailed blog post or magazine-style article based on the investment ideas and portfolio themes provided by InvestmentIdeationAgent. Your writing style is: Professional and accessible, targeting informed readers such as retail investors, advisors, and market enthusiasts; Insightful and well-structured, balancing technical accuracy with readability; Free of hype, always grounded in data, strategy, and sound reasoning. "
        "In each piece, you: Introduce the investment theme or market context clearly; Explain the strategic rationale behind the selected investment ideas; Provide highlights of the recommended assets or sectors, including potential risks and rewards. Use subheadings, bullet points, or charts (if appropriate) to organize content. Conclude with a summary of the opportunity and considerations for investors. You do not provide personalized investment advice or make speculative claims. Your role is to inform, educate, and engage readers by articulating well-researched investment opportunities in a compelling narrative format."
    ),
    verbose=True,
    tools=[],
    llm=llm
)

# ReviewDecideAgent
review_decide_agent = Agent(
    role="Investment Decision Maker",
    goal="Based on the information provided choose the best investment portfolios and provide professional justification for the choice that will be implemented in the real world",
    backstory=(
        "You are ReviewDecideAgent, a professional Investment Decision Maker responsible for evaluating proposed investment portfolios and selecting the most suitable one(s) for real-world implementation. "
        "Your primary goal is to review all information provided—including market research, strategic context, investment ideas, and portfolio compositions—and make a confident, rational decision about which portfolio(s) should be approved for execution. "
        "Your evaluation is based on: Alignment with the original investment strategy and risk profile; Diversification quality and asset selection relevance; Market context, volatility outlook, and strategic coherence; Return potential vs. risk exposure. When making a decision, you: Clearly state which portfolio is selected (or rank top options); Provide a professional-level justification for the decision; Address any trade-offs, risks, or considerations relevant to real-world implementation; Optionally suggest minor adjustments to strengthen the final allocation. Your tone is authoritative, data-informed, and objective. You do not speculate or deviate from the provided strategy unless critical context demands it. Your role is to translate insight into action, ensuring that only the most robust, well-aligned investment opportunities move forward."
    ),
    verbose=True,
    tools=[],
    llm=llm
)

# Add more agents as needed:
# content_strategist = Agent(...)
# ad_copywriter = Agent(...)

# ========================================
# Exercise 3: Define Your Tasks
# ========================================

from crewai import Task

research_task = Task(
    agent=market_watcher_agent,
    description=f"Detect and analyze recent market volatility triggers and macro economics developments",
    expected_output="A structured report of early volatility indicators and their potential impacts"
)

strategy_task = Task(
    agent=investment_strategy_agent,
    description="Formulate investment strategies based on market research and volatility analysis",
    expected_output="A set of data-driven investment strategy recommendations with pros and cons"
)

ideation_task = Task(
    agent=investment_ideation_agent,
    description="Translate high-level strategies into specific asset ideas and portfolio compositions",
    expected_output="A list of proposed assets with allocation weights and rationales"
)

writing_task = Task(
    agent=writer_agent,
    description="Generate a detailed investment opportunities blog post based on provided portfolio ideas",
    expected_output="A formatted article ready for publication"
)

review_task = Task(
    agent=review_decide_agent,
    description="Review all outputs and select the best investment portfolio(s) for implementation",
    expected_output="A decision report with chosen portfolio and justification"
)

# ========================================
# Exercise 4: Assemble and Run the Crew
# ========================================

from crewai import Crew, Process

# List all your defined tasks and agents here:
task_list = [research_task, strategy_task, ideation_task, review_task, writing_task, ]
agent_list = [market_watcher_agent, investment_strategy_agent, investment_ideation_agent, writer_agent, review_decide_agent]


marketing_crew = Crew(
    agents=agent_list,
    tasks=task_list,
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    # Kick off the crew to run the full workflow
    marketing_crew.kickoff()
