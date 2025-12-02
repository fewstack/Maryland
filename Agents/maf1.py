import asyncio
import os
from dotenv import load_dotenv
from agent_framework import ChatAgent
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential

# Load environment variables from .env file
load_dotenv()

async def main():
    # Get the Azure AI project endpoint from environment variable
    project_endpoint = os.environ.get("Azure_AI_Foundry_project_endpoint")
    Azure_Ai_Model_Deployment = os.environ.get("Azure_Ai_Model_Deployment")
    
    if not project_endpoint:
        raise ValueError("Please set the 'Azure_AI_Foundry_project_endpoint' environment variable.")
    
    async with (
        AzureCliCredential() as credential,
        
        ChatAgent(
            chat_client=AzureAIAgentClient(
                async_credential=credential,
                project_endpoint=project_endpoint
            ),
            instructions="You are good at telling jokes."
        ) as agent,
    ):
        result = await agent.run("Tell me a joke about a pirate.")
        print(result.text)

if __name__ == "__main__":
    asyncio.run(main())