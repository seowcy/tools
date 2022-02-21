import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.event("message")
def handle_message_events(body, say):
    print(body)
    user = body['event']['user']
    recv_text = body['event']['text']
    say(channel=user, text="Received: %s" % recv_text)
    # logger.info(body)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()