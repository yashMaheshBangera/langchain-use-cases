from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain.chat_models import init_chat_model


model = init_chat_model(
        "microsoft/Phi-3-mini-4k-instruct",
        model_provider="huggingface",
        temperature=0.7,
        max_tokens=1024
    )

messages = [
    SystemMessage(content="Extract the entities in JSON format from the user's phrase"),
    
    # --- First Example ---
    HumanMessage(content="The elephant is sleeping"),
    AIMessage(content="Entities: {\"animal\": \"elephant\", \"action\": \"sleeping\"}"),

     # --- First Example ---
    HumanMessage(content="The dog is barking."),
    AIMessage(content="Entities: {\"animal\": \"dog\", \"action\": \"barking\"}"),

    # --- THE USER PROMPT (The one we want the model to answer) ---
    HumanMessage(content="The monkey is eating an apple.")

]
response = model.invoke(messages)

print(response.content)