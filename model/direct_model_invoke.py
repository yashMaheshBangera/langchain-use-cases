import os
from langchain.chat_models import init_chat_model

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "<HUGGINGFACEHUB_API_TOKEN>"

def test_chat_model():

    model = init_chat_model(
        "microsoft/Phi-3-mini-4k-instruct",
        model_provider="huggingface",
        temperature=0.7,
        max_tokens=1024,
    )
    response = model.invoke("How do I create a local server?")
    print(response)
    return None

if __name__ == "__main__":
    test_chat_model()