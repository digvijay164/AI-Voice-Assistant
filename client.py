    
from openai import OpenAI

from openai import OpenAI
client = OpenAI(api_key = "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")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)