from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/fetch-data", methods=["POST"])
def fetch_images():

    data = request.json

    url = "https://api.unsplash.com/search/photos?"

    auth = {"Authorization": "CLIENT ID OMITTED FROM GITHUB REPO"}

    search_term = {"query": data}
    
    api_call_resp = requests.get(url, params = search_term, headers=auth)

    return api_call_resp.json()



@app.route("/fetch-limit", methods=["POST"])
def fetch_limit():

    data = request.json

    url = "https://api.unsplash.com/search/photos?"

    auth = {"Authorization": "CLIENT ID OMITTED FROM GITHUB REPO"}

    search_term = {"query": data}
    
    api_call_resp = requests.get(url, params = search_term, headers=auth)

    call_limit = dict(api_call_resp.headers)

    return jsonify(call_limit)



@app.route("/fetch-download", methods=["POST"])
def fetch_download():

    data = request.json

    auth = {"Authorization": "CLIENT ID OMITTED FROM GITHUB REPO"}

    image_request = requests.get(data, headers=auth, stream = True)

    return image_request.json()