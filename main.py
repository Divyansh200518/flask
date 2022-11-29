from flask import Flask, jsonify
import os
from jiosaavn.Sync import searchSong
from jiosaavn.Sync import song

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    user_query = str(request.args.get('search'))
    search = searchSong(user_query)
    result = song(id=search[0]["id"])['audioUrls']["320_KBPS"]
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅","url":result})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
