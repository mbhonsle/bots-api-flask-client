# oauth request constants
GRANT_TYPE = "urn:ietf:params:oauth:grant-type:jwt-bearer"
CHATBOT_SCOPE = "chatbot_api"

# bots URI template
INIT_CHAT_URI="/v5.0.0/bots/{}/sessions"
SEND_MESSAGES_URI="/v5.0.0/sessions/{}/messages"
END_CHAT_URI="/v5.0.0/sessions/{}"

# bots requests constants
ORG_ID_HEADER_KEY="X-Org-Id"
END_SESSION_HEADER_KEY="X-Session-End-Reason"