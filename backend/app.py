from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load a code-generation model from Hugging Face (e.g., Salesforce/codegen-350M-mono)
generator = pipeline('text-generation', model='Salesforce/codegen-350M-mono')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    # Generate code based on the provided prompt
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return jsonify(result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
