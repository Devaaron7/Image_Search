from flask import Flask, request, jsonify
import requests
from flask_cors import CORS, cross_origin
from UnsplashApi import Connect, os

app = Flask(__name__)

@app.route("/wake", methods=["POST"])
@cross_origin()
def wake():

    data = request.json

    if data["alarm"] == "wake up":
        return "awake"
    else:
        return "sleeping"


@app.route("/start", methods=["POST"])
@cross_origin()
def start():

    data = request.json

    session = Connect(data["name"])

    session.start()

    if isinstance(session.start(), str) == True:
        return session.start(), 400

    else:

        session.filter_results()

        session.download_images(session.filtered_list)

        credits_left = {"credits": session.limit_results}

        session.dl_list_to_return.append(credits_left)

        return jsonify(session.dl_list_to_return)



@app.route("/fetch-data", methods=["POST"])
def fetch_images():

    data = request.json

    url = "https://api.unsplash.com/search/photos?per_page=3"

    auth = {"Authorization": "Client-ID CLIENT SECERT OMITTED"}

    search_term = {"query": data}
    
    api_call_resp = requests.get(url, params = search_term, headers=auth)

    return api_call_resp.json()



@app.route("/fetch-limit", methods=["POST"])
def fetch_limit():

    data = request.json

    url = "https://api.unsplash.com/search/photos?per_page=3"

    auth = {"Authorization": "Client-ID CLIENT SECERT OMITTED"}

    search_term = {"query": data}
    
    api_call_resp = requests.get(url, params = search_term, headers=auth)

    call_limit = dict(api_call_resp.headers)

    return jsonify(call_limit)



@app.route("/fetch-download", methods=["POST"])
def fetch_download():

    data = request.json

    auth = {"Authorization": "Client-ID CLIENT SECERT OMITTED"}

    image_request = requests.get(data, headers=auth, stream = True)

    return image_request.json()