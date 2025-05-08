
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query')
    # Dummy response for demonstration
    return jsonify({'answer': f'Fake answer to: {query}'})

if __name__ == '__main__':
    app.run(debug=True)
