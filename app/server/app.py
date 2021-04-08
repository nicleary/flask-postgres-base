from typing import List, Dict
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return {"chungus": "no"}

if __name__ == '__main__':
    app.run(host='0.0.0.0')