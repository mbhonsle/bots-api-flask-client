import logging
import requests
from app import app
from flask import request
from app.auth import get_oauth_access_token
from app.constants import INIT_CHAT_URI, SEND_MESSAGES_URI, END_CHAT_URI

@app.route("/start/<bot_id>", methods=["POST"])
def init(bot_id):
    request_url = get_request_url(INIT_CHAT_URI.format(bot_id))
    return send(request.json, request_url)

@app.route("/chat/<session_id>", methods=["POST"])
def chat(session_id):
    request_url = get_request_url(SEND_MESSAGES_URI.format(session_id))
    return send(request.json, request_url)

@app.route("/end/<session_id>", methods=["DELETE"])
def end(session_id):
    request_url = get_request_url(END_CHAT_URI.format(session_id))
    return "ending chat: " + session_id

def send(data, url):
    headers = get_headers()
    # return requests.post(url, headers=headers, data=data)
    "data: {}, headers: {}, url: {}".format(data, headers, url)

def get_request_url(uri):
    return app.config.get("BOTS_SERVER_URL") + uri

def get_headers():
    token = get_oauth_access_token()
    return {
        "Authorization": "Bearer " + token,
        "Content-Type":"application/json",
        "Accept": "application/json"
    }

def configure_logging():
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

if __name__ == "__main__":
    configure_logging()
    app.run(debug=True)