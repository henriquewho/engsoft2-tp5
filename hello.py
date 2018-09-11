import os
from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Teste Geraldo1!</hi>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
