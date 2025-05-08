# agent.py
import boto3
from autogen.agent_tools import Agent  # Updated import path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class BedrockAgent(Agent):
    def __init__(self, name, model_id, region_name='us-east-1'):
        super().__init__(name)
        self.model_id = model_id
        try:
            self.client = boto3.client('bedrock-runtime', region_name=region_name)
        except Exception as e:
            logging.error(f"Error initializing Bedrock client: {e}")
            raise

    def generate_response(self, prompt):
        try:
            response = self.client.invoke_model(
                modelId=self.model_id,
                contentType='text/plain',
                accept='text/plain',
                body=prompt.encode('utf-8')
            )
            result = response['body'].read().decode('utf-8')
            return result
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "I'm sorry, but I couldn't process your request at this time."
