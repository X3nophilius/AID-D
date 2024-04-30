# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

stream = client.chat.completions.create(
  model="Lewdiculous/InfinityRP-v1-7B-GGUF-IQ-Imatrix",
  messages=[
    {"role": "system", "content": "you are a helpfull ai assistant"},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
  stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

print("""


""")

stream = client.chat.completions.create(
  model="Lewdiculous/InfinityRP-v1-7B-GGUF-IQ-Imatrix",
  messages=[
    {"role": "system", "content": "you are a helpfull ai assistant"},
    {"role": "user", "content": "what was my previouse request?"}
  ],
  temperature=0.7,
  stream=True
)


for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")