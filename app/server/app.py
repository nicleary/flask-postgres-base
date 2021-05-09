from typing import List, Dict
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return {"chungus": "perhaps"}

app.run(host='0.0.0.0')