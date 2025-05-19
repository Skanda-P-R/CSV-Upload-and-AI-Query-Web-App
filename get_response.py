from groq import Groq
import os

client = Groq(
    api_key=os.getenv('groq_api'),
)

def groq_response(data_csv,query):
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

    return (chat_completion.choices[0].message.content)