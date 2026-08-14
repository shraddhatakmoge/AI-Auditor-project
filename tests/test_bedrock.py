from app.llm.bedrock import BedrockLLM


llm = BedrockLLM()

response = llm.invoke(
    "Explain Retrieval-Augmented Generation in one sentence."
)

print(response)