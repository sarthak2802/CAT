import os
from flask import Flask, request, jsonify, send_from_directory
import openai

app = Flask(__name__, static_folder='../frontend')

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/solve-question', methods=['POST'])
def solve_question():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Use OpenAI's GPT model to solve the question and provide explanation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Solve this CAT question and provide a detailed explanation: {question}",
        max_tokens=300
    )

    answer = response.choices[0].text.strip()

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
