from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-1.7B-Instruct")
print(pipe(messages))
