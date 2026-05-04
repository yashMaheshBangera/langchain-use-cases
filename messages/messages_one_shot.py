from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain.chat_models import init_chat_model


model = init_chat_model(
        "microsoft/Phi-3-mini-4k-instruct",
        model_provider="huggingface",
        temperature=0.7,
        max_tokens=1024
    )

messages = [
    SystemMessage(content="Translate the user's phrase into a short summary followed by 3 relevant emojis."),
    
    # --- THE ONE SHOT (Example) ---
    HumanMessage(content="I am going to the beach for a vacation."),
    AIMessage(content="Heading to the coast for some relaxation. 🏖️🌊☀️"),

    # --- THE USER PROMPT (The one we want the model to answer) ---
    HumanMessage(content="I am planning a picnic for next week.")

]
response = model.invoke(messages)

print(response.content)