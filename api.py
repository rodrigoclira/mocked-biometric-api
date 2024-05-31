from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ENDPOINT = "http://127.0.0.1:5000"
TOKEN_EXAMPLE = "0facc635-30a1-4bb0-a09d-24b2fe867af3"

@app.route('/api/generate_token', methods=['POST'])
def generate_token():
    data = request.get_json()  # Get the JSON data from the request
    
    # Create a JSON response
    response = {
        "token": f"{TOKEN_EXAMPLE}",
        "expires_at": "2024-05-19T21:31:42.515070",
        "capture_url": f"{ENDPOINT}/capture_photo?token={TOKEN_EXAMPLE}"
    }

    return jsonify(response)


# create a endpoint that receive a variable in the url
@app.route('/api/checar_registro_biometria', methods=['GET'])
def checar_registro_biometria():
    uid = request.args.get('id')

    response = {
        "message": f"Sucesso! Biometria do id {uid} foi registrada."
    }

    return jsonify(response)

@app.route('/api/login_request', methods=['GET'])
def login_request():
    token = request.args.get('token')

    response = {
        "capture_url": f"{ENDPOINT}/capture_login?token={token}"
    }

    return jsonify(response)


@app.route('/api/check_login', methods=['GET'])
def check_login():
    uid = request.args.get('id')

    response = {
            "message": f"Sucesso! Login do id {uid} foi bem-sucedido."

    }

    return jsonify(response)


if __name__ == '__main__':
    # run the app in a different port
    app.run(port=5001)
