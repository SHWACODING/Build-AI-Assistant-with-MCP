"""
Simple Chat Example Using MCPAgent with Built-in Conversation Memory.

This Example Demonstrates hw to use the MCPAgent with its built-in Conversation History Capabilities
for better Contextual Interactions

"""

import asyncio

from langchain_groq import ChatGroq

from mcp_use import MCPAgent, MCPClient

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


async def run_memory_chat():
    """
    Run a Chat Using MCPAgent's Built-in Conversation Memory.
    """

    ## Config File Path
    config_file = "mcp_servers.json"

    print("🧨Initializing The Chat...")

    ## Create MCP Client and Agent With Memory Enabled
    client = MCPClient.from_config_file(config_file)

    ## Initialize Groq Chat Model LLM
    llm = ChatGroq(model="llama-3.3-70b-versatile")

    ## Create Agent With memory_enabled=True
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True   ## Enable Built-In Conversation Memory
    )

    print("\n============== Interactive MCP Chat ==============\n")
    print("Type 'exit' or 'quit' To End The Conversation")
    print("Type 'clear' To Clear The Conversation History")
    print("\n=" * 55)

    try:
        ## Main Chat Loop
        while True:
            ## Get User Input ->
            user_input = input("\n😎 YOU 👉 ")

            ## Check if exit or quit Command
            if user_input.lower() in ["exit", "quit"]:
                print("🙌 Ending Conversation...")
                break

            ## Check for clear History Command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("✅ Conversation History Cleared..")
                continue

            ## Get Response From Agent
            print("\n💭 Assistant 👉 ", end="", flush=True)

            try:
                ## Run the Agent With The User Input (Memory Handled Automatic)
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"\nError: {str(e)}")
        
    finally:
        ## Clean Up
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
