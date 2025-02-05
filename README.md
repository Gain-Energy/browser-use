# Gain.Energy Browser Agent Development

This repository is forked from [browser-use](https://github.com/browser-use/browser-use) and customized specifically for developing AI agents for the Upstrima Oil and Gas Platform. Our focus is on creating intelligent browser automation agents that help petroleum engineers interact with and extract data from the platform efficiently.

## Quick Start

Install required packages:

```bash
pip install browser-use langchain-openai
```

Install playwright:

```bash
playwright install
```

Configure your environment:

```bash
OPENAI_API_KEY=your_api_key
BROWSER_USE_LOGGING_LEVEL=info
```

## Example Implementation

Here's a basic example of how to create an agent for interacting with the platform:

```python
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

asyncio.run(main())
```

## Key Features for Petroleum Engineers

- **Automated Data Capture**: Screenshot capabilities for well data visualizations and technical reports
- **Intelligent Navigation**: GPT-4 powered understanding of complex oil & gas interfaces
- **Quality Assurance**: Automatic validation of data visibility and error handling
- **Custom Actions**: Specialized interactions for oil & gas specific workflows

## Common Use Cases

1. **Well Data Collection**
   - Production rates monitoring
   - Pressure readings capture
   - Temperature logs extraction

2. **Reservoir Analysis**
   - Historical production data analysis
   - Performance graph capture
   - Simulation results download

3. **Equipment Monitoring**
   - Status indicator checks
   - Maintenance alert capture
   - Performance metrics documentation

## Documentation

For detailed documentation on developing agents for specific use cases, see:
- [Upstrima Browser Agent Guide](examples/use-cases/upstrima_browser_agent_README.md)

## Development Focus

This fork focuses on:
- Creating specialized agents for petroleum engineering workflows
- Automating common Upstrima platform interactions
- Developing industry-specific validation and data processing
- Implementing secure authentication and data handling

## Security and Compliance

All agents developed using this framework must adhere to:
- Industry standard security protocols
- Data protection requirements
- Access control policies
- Audit trail maintenance

## Contributing

When contributing to this fork, please ensure your changes are focused on improving the functionality for petroleum engineering use cases and Upstrima platform integration.

---
Forked from [browser-use](https://github.com/browser-use/browser-use) and customized by Gain.Energy for Upstrima Oil and Gas Platform development.
