from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv
import os
import asyncio

load_dotenv(find_dotenv())

mcp_token = os.getenv("mcp_token")

async def main():
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY set nahi hai!")
        return
    
    print("🚀 Weather Agent starting...\n")

    async with MCPServerStdio(
    params={ "command": "/path/to/github-mcp-server",
        "args": ["stdio"],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": mcp_token}
          }
    ) as mcp_server:
    
    

        print("✅ Connected to MCP Server!\n")

        agent = Agent(
            name="personal AI Assistant",
            instructions="""
            You are a personal AI assistant that provides general information related the user's queries.
            """,
            mcp_servers=[mcp_server]
        )

        result = await Runner.run(
            agent,
            input="tell me about the how many python repositories are there in github of AreebaxIrfan?"
        )
        print(f"🤖 Agent: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())



