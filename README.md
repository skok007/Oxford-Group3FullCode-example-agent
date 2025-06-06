# Example Agent: Multi-Agent Investment Strategy AI

This project demonstrates a multi-agent AI system for investment research, strategy, ideation, content generation, and decision-making. It leverages [CrewAI](https://github.com/joaomdmoura/crewai).

## Agents

- **MarketWatcherAgent**: Gathers and analyzes financial news and volatility triggers.
- **InvestmentStrategyAgent**: Forms investment strategies based on research.
- **InvestmentIdeationAgent**: Generates actionable investment ideas and portfolio compositions.
- **WriterAgent**: Produces detailed investment opportunity articles.
- **ReviewDecideAgent**: Selects the best portfolios and provides professional justifications.

## Requirements

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- API keys for required services (e.g., OpenAI, Serper)

## Setup

1. **Install uv**  
   Follow the instructions at [uv installation](https://github.com/astral-sh/uv#installation).

3. **Create a `.env` file**  
   Add your API keys and any other required environment variables. Example:
   ```
   OPENAI_API_KEY=your-openai-key
   SERPER_API_KEY=your-serper-key
   # Add other keys as needed
   ```

4. **Run the agent**  
   ```sh
   uv run main.py
   ```