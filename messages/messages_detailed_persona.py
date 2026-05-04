from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

model = init_chat_model(
        "microsoft/Phi-3-mini-4k-instruct",
        model_provider="huggingface",
        temperature=0.7,
        max_tokens=1024
    )

system_msg = SystemMessage("""
You are a senior Python developer with expertise in web frameworks.
Always provide code examples and explain your reasoning.
Be concise but thorough in your explanations.
""")

messages = [
    system_msg,
    HumanMessage("How do I create a REST API?")
]
response = model.invoke(messages)
print(response.content)