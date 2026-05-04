from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

model = init_chat_model(
        "microsoft/Phi-3-mini-4k-instruct",
        model_provider="huggingface",
        temperature=0.7,
        max_tokens=1024
    )

system_msg = SystemMessage("You are a helpful assistant.")
human_msg = HumanMessage("Hello, how are you?")

# Use with chat models
messages = [system_msg, human_msg]
response = model.invoke(messages)  # Returns AIMessage
print(response)