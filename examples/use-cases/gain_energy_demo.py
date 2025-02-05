from browser_use import Agent
from langchain_openai import ChatOpenAI
import asyncio

async def main():
    llm = ChatOpenAI(model='gpt-4o')
    agent = Agent(
        task="""Go to https://gain.energy and perform the following steps:
1. Wait for the main page to fully load and take a screenshot of the hero section
2. Scroll down slowly to see the product features and take a screenshot
3. Scroll further to see the pricing section and take a final screenshot""",
        llm=llm,
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
