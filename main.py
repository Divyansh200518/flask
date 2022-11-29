# from flask import Flask, jsonify
# import os

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


# if __name__ == '__main__':
#     app.run(debug=True, port=os.getenv("PORT", default=5000))
from flask import *
import json
from flask_cors import CORS, cross_origin

from jiosaavn.Sync import searchSong

from jiosaavn.Sync import song


app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])


def request_page():

    user_query = str(request.args.get('search'))
    if len(user_query) > 0 and user_query != "None":
        search = searchSong(user_query)
        result = song(id=search[0]["id"])['audioUrls']["320_KBPS"]
        print(result)
        data_set = {'Page': 'Request', 'Message': f"Successfully got the request for {user_query}",'answer':result}
        json_dump = json.dumps(data_set)
        return json_dump
    else:
        data_set = {'Page': 'Request', 'Message': "No requests yet",'answer':": )"}
        json_dump = json.dumps(data_set)
        return json_dump


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
