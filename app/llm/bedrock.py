import os

import boto3
from dotenv import load_dotenv


load_dotenv()


class BedrockLLM:

    def __init__(self):

        self.client = boto3.client(
            "bedrock-runtime",
            region_name=os.getenv(
                "AWS_REGION",
                "eu-north-1"
            )
        )

        self.model_id = "amazon.nova-lite-v1:0"

    def invoke(self, prompt: str) -> str:

        response = self.client.converse(
            modelId=self.model_id,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            inferenceConfig={
                "temperature": 0,
                "maxTokens": 512
            }
        )

        return response["output"]["message"]["content"][0]["text"]