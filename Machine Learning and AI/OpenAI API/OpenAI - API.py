from openai import OpenAI
from tenacity import (retry, wait_random_exponential, stop_after_attempt)

client = OpenAI(api_key="Enter your Key here")

@rety(wait=wait_random_exponential(min=1, max=60),stop=stop_after_attempt)
def get_response(model,message):
  response = client.chat.completions.create(
    model=model
    messages=message,
  )

  return print(response.choices[0].message.content)

