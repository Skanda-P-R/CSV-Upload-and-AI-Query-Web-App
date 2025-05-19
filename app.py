from flask import Flask, render_template, request, jsonify
from get_response import groq_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def response():
    data = request.get_json()
    data_csv = data.get("csvData", "")
    query = data.get("query", "")

    response = groq_response(data_csv,query)    

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
