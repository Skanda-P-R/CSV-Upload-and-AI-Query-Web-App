from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    data_csv = data.get("csvData", "")
    query = data.get("query", "")

    client = Groq(
        api_key=os.getenv('groq_api'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI which gives answers based on the CSV file and the Query asked by the user."
            },
            {
                "role": "user",
                "content": f"CSV File:\n{data_csv}\n\nQuery: {query}",
            }
        ],
        model="gemma2-9b-it",
    )

    return jsonify({"response": chat_completion.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
