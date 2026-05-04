# Langchain use cases

## Sample use case 1 :page_facing_up:

### Model invocation

The first use-case lies under the `model` dir where we test direct invocation of model using the `langchain-huggingface` provider in python. 

You can read more here : https://docs.langchain.com/oss/python/langchain/models#huggingface
<br>
Model used : Microsoft -> Phi-3-mini-4k-instruct [HuggingFace Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
<br>
Generation configurations : 
```
temperature : 0.7  #Higher the value, more non-deterministic the output ( min 0, max 1 )
max_tokens : 1024  
```
To get started simply run :
```
cd model/
python direct_model_invoke.py
```

## Sample use case 2 :page_facing_up:

### Messages

Here, we test the messages protocol offered by Langchain. You can read more about it here : https://docs.langchain.com/oss/python/langchain/messages

We test the same model using different prompt engineering guidelines, namely:
1. System + Human Prompting Sample : messages_basic.py
2. One-Shot prompting : messages_one_shot.py
3. Few-Shot prompting : messages_few_shot.py
4. Detailed Persona : messages_detailed_persona.py

To get started simply run :
```
cd messages/
python messages_<suffix>.py
```

## Sample use case 3 :page_facing_up:

### Tool Calling

Under `tools` dir, you can find a sample of invocation with a tool using the following model: `Qwen/Qwen2.5-7B-Instruct`. To further restrict tool calling and creative responses, we use `temperature:0.01`.


