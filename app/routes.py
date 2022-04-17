import logging
import requests
import json
from app import app
from flask import request
from app.auth import get_oauth_access_token
from app.constants import INIT_CHAT_URI, SEND_MESSAGES_URI, END_CHAT_URI, ORG_ID_HEADER_KEY, END_SESSION_HEADER_KEY

@app.route("/start/<bot_id>", methods=["POST"])
def init(bot_id):
    request_url = get_request_url(INIT_CHAT_URI.format(bot_id))
    response = send(request.json, request_url)
    return response

@app.route("/chat/<session_id>", methods=["POST"])
def chat(session_id):
    request_url = get_request_url(SEND_MESSAGES_URI.format(session_id))
    return send(request.json, request_url)

@app.route("/end/<session_id>", methods=["DELETE"])
def end(session_id):
    request_url = get_request_url(END_CHAT_URI.format(session_id))
    headers = get_headers()
    headers[END_SESSION_HEADER_KEY] = request.headers.get(END_SESSION_HEADER_KEY)
    response = requests.delete(request_url, headers=headers)
    validate_response(response)
    return json.loads(response.text)

def send(data, url):
    headers = get_headers()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    validate_response(response)
    return json.loads(response.text)

def validate_response(response):
    # check status code
    if response.status_code != 200:
        raise ValueError("Invalid response code from Bot server.")    


def get_request_url(uri):
    return app.config.get("BOTS_SERVER_URL") + uri

def get_headers():
    token = get_oauth_access_token()
    orgId = app.config.get("ORG_ID")
    return {
        "Authorization": "Bearer " + token,
        "Content-Type":"application/json",
        "Accept": "application/json",
        ORG_ID_HEADER_KEY: orgId 
    }

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

if __name__ == "__main__":
    configure_logging()
    app.run()