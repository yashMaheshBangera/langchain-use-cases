from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage,AIMessage
import json

@tool
def get_sum(number1: int,number2: int) -> str:
    """Get the sum of 2 numbers."""
    total_value = number1 + number2
    return f"The total value is {total_value}."

model = init_chat_model(
        "Qwen/Qwen2.5-7B-Instruct",
        model_provider="huggingface",
        temperature=0.01,
        max_tokens=1024,
    )

model_with_tools = model.bind_tools([get_sum])
messages = [
    SystemMessage(content=(
        "You are a helpful assistant. To answer math questions, "
        "you MUST call the 'get_sum' tool. Respond ONLY with a "
        "tool call in JSON format."
    )),
    HumanMessage(content="What's the sum of 50 and 45?"),
]

response = model_with_tools.invoke(messages)
print("========================================================")
print(response)
print("========================================================")

if "<|im_start|>assistant" in response.content:
    json_str = response.content.split("<|im_start|>assistant")[-1].strip()
    print(json_str)
else:
    json_str = response.content.strip()

try:
    tool_call_data = json.loads(json_str)
    print("========================================================")
    print(f"Tool: {tool_call_data['tool']}")
    print(f"Args: {tool_call_data['args']}")
    print("========================================================")
except json.JSONDecodeError as e:
    print(f"Failed to parse: {json_str}")
