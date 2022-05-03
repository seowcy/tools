import os
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

results = {}
# Load results
with open("asp_results.json", 'rb') as f:
    results = {**results, **json.load(f)}
with open("csharp_results.json", 'rb') as f:
    results = {**results, **json.load(f)}
with open("java_results.json", 'rb') as f:
    results = {**results, **json.load(f)}


@app.event("message")
def handle_message_events(body, say):
    print(body)
    user = body['event']['user']
    recv_text = body['event']['text']
    if recv_text.lower() in results.keys():
        resp = results[recv_text.lower()]
        say(channel=user, text="```Title: %s\n```\n```Description:\n%s\n```\n```Impact:\n%s\n```\n```Mitigation:\n%s```\n" % (resp['title'], resp['desc'], resp['impact'], resp['mitigation']))
    else:
        say(channel=user, text="Received: %s" % recv_text)
    # logger.info(body)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()