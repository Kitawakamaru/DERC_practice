import slack

OAUTH_TOKEN = 'xoxb-1120138671520-3646407771236-ozLyUzXZMbW1z02zzsQGXqsN'
CHANNEL_NAME = 'U0136T5J0HX'

client = slack.WebClient(token=OAUTH_TOKEN)

response = client.chat_postMessage(
    channel=CHANNEL_NAME,
    text="chat bot test message")
