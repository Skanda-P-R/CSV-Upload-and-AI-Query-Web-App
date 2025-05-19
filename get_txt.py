import pandas as pd
from groq import Groq
import os

data = pd.read_csv('test.csv')

data_csv = data.to_csv(index=False)

print(data_csv)

query = "for the credit transaction type, calculate the aggregated balance value"

client = Groq(
    api_key=os.getenv('groq_api'),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an AI which gives answers based on the CSV file and the Query asked bby the user."
        },
        {
            "role": "user",
            "content": "CSV File: " + data_csv + "\n\nQuery: " + query + "\n",
        }
    ],
    model="gemma2-9b-it",
)

print(chat_completion.choices[0].message.content)