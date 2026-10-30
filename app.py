from flask import Flask
import socket

app = Flask(__name__)
VERSION = "v1"

@app.route("/")
def home():
    return (f"<h1 style='font-family:sans-serif'>Demo First App {VERSION}</h1>"
            f"<p>Served by pod: {socket.gethostname()}</p>")

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
