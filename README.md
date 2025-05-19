# CSV Upload & AI Query Web App

This is a simple Flask-based web application that allows users to upload a CSV file, enter a query, and receive an AI-generated response based on the CSV data. The backend uses the [Groq API](https://console.groq.com/) with the `gemma2-9b-it` model to process the input.

## Features

- Upload a `.csv` file
- Input a natural language query
- Get AI-generated insights or responses based on your data
- Markdown-rendered responses
- Clean and minimal interface

## Demo

![image](https://github.com/user-attachments/assets/8b758c13-0dc2-40d5-a0db-68450c34a144)

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **AI API**: [Groq API](https://groq.com/)
- **Model**: `gemma2-9b-it`

---

## Getting Started

### Prerequisites

- Python 3.7+
- A Groq API key (get it from [https://console.groq.com](https://console.groq.com))

### Installation

1. **Clone the repo**

```
https://github.com/Skanda-P-R/CSV-Upload-and-AI-Query-Web-App.git
cd CSV-Upload-and-AI-Query-Web-App
```

2. **Create and activate a virtual environment (optional but recommended)**
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```
pip install flask groq
```

4. **Set your environment variable**
```
export groq_api=your_groq_api_key   # On Windows: set groq_api=your_groq_api_key
```

5. **Run the app**
```
python app.py
```

6. **Open your browser and go to: http://localhost:5000**

---

### File Structure
```
.
├── app.py                # Flask backend
├── templates/
│   └── index.html        # Main HTML file
├── static/
│   ├── script.js         # Frontend logic
│   └── style.css          
├── README.md             # Project documentation
```

---

### How It Works
* The user uploads a .csv file.
* The frontend reads the file content as text and sends it to the backend.
* A query is also sent along with the CSV data.
* The Flask backend constructs a prompt for the AI using both the file and the query.
* The AI model (via Groq API) returns a response.
* The frontend parses and displays the response using Markdown.

---
