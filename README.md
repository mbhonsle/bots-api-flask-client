# Einstein Bots V5 API Python Client

This is a simple Python Flask server application to interact with the Einstein Bots V5 API.

## Usage

1. update the ./config/config.cfg
   - add an appropriate value for ORG_ID
   - add an appropriate value for BOTS_SERVER_URL
   - add an appropriate value for JWT (this will be exchanged with login server for the OAuth access token)
   - add an appropriate value for OAUTH_SERVER

2. to start a chat use the following request:
```
curl --location --request POST 'http://127.0.0.1:5000/start/<your-bot-id>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "forceConfig": {
        "endpoint": "<your org's instance URL>"
    },
    "externalSessionKey": "<UUID>"
}'
```
Note down the `sessionId` from the response

3. to continue chatting with the bot on an existing `sessionId`:
```
curl --location --request POST 'http://127.0.0.1:5000/chat/<sessionId from the start request's response>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "message": {
        "type": "text",
        "text": "<any text>",
        "sequenceId":1
    }
}'
```

4. to end a chat session:
```
curl --location --request DELETE 'http://127.0.0.1:5000/end/<sessionId from the start request's response>' \
--header 'Content-Type: application/json' \
--header 'X-Session-End-Reason: UserRequest'
```