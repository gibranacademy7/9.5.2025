from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "hello"}
  ]
)

print(completion.choices[0].message.content);