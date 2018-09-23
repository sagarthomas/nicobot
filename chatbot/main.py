from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    return ''

@app.route('/train', methods=['POST'])
def train():
    return ''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)