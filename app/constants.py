# oauth request constants
GRANT_TYPE = "urn:ietf:params:oauth:grant-type:jwt-bearer"
CHATBOT_SCOPE = "chatbot_api"

# bots URI template
INIT_CHAT_URI="/bots/{}/sessions"
SEND_MESSAGES_URI="/sessions/{}/messages"
END_CHAT_URI="/sessions/{}"