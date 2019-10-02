import os

from flask import Flask
app = Flask(__name__)
base_path = os.path.dirname(os.path.abspath(__file__))
openssl_path = os.path.join(base_path, '..', 'openssl')


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', ssl_context=(os.path.join(openssl_path, 'cert.pem'), os.path.join(openssl_path, 'key.pem')))
