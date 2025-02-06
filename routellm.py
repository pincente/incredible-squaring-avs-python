import openai
import os

client = openai.OpenAI(
  base_url="https://api.openai.com/v1",
  # Required but ignored
  api_key=os.environ.get("OPENAI_API_KEY")
)
response = client.chat.completions.create(
  # "Use the MF router with a threshold of 0.116"
  model="router-mf-0.116",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

def inference(prompt):
    response = client.chat.completions.create(model="router-mf-0.116", messages=[{"role": "user", "content": prompt}])
    print(response.choices[0].message.content)
    return response.choices[0].message.content
