from openai import OpenAI

client=OpenAI()

res=client.chat.completions.create(
    model="gpt-6-luna",
    messages=[
        {
            "role":"user",
            "content":"write about software developer?"
        }
    ]
)

print(res.choices[0].message.content)
