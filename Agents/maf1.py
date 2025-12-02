import asyncio
from agent_framework import ChatAgent
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential
import os
import dotenv
dotenv.load_dotenv()

Azure_AI_Foundry_project_endpoint = os.getenv("Azure_AI_Foundry_project_endpoint")
Azure_AI_Model_Deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")


async def main():
    async with AzureCliCredential() as credential:
        async with ChatAgent(
            chat_client=AzureAIAgentClient(
                async_credential=credential,
                project_endpoint=Azure_AI_Foundry_project_endpoint,
                model_deployment_name=Azure_AI_Model_Deployment
            ),
            instructions="You are a dental insurance agent and analyst"
        ) as agent:
            result = await agent.run("How are dental insurance carriers doing in 2025?")
            print(result.text)

if __name__ == "__main__":
    asyncio.run(main())