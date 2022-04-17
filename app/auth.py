import requests
import json
from flask import current_app as app
from app.constants import CHATBOT_SCOPE, GRANT_TYPE

def validate_response(response):
    # check status code
    if response.status_code != 200:
        raise ValueError("Invalid response code from Auth server.")    

    data = json.loads(response.text)
    # check the oauth token
    if data["access_token"] == "":
        raise Exception("No access token returned")

    # check the scope
    if CHATBOT_SCOPE not in data["scope"]:
        raise Exception("Invalid scopes")

def get_oauth_access_token():
    config = app.config
    if config.get("OAUTH_TOKEN") != "":
        return config.get("OAUTH_TOKEN")
    else:
        # exchange JWT for OAuth token
        data = {"assertion": config.get("JWT"), "grant_type":GRANT_TYPE}
        response = requests.post(config.get("OAUTH_SERVER"), data=data)
        validate_response(response)
        return json.loads(response.text)["access_token"]