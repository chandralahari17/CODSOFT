from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.json.get('message', '').lower()
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(message):
    if 'hello' in message:
        return "Hi there! How can I help you today?"
    elif 'how are you' in message:
        return "I'm just a bot, but I'm here to help you!"
    elif 'bye' in message:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure I understand. Can you please rephrase?"

if __name__ == '__main__':
    app.run(debug=True)











