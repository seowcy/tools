from slack_sdk import WebClient
import argparse
import os

SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]


def send_message(client, user, message):
	response = client.chat_postMessage(channel=user, text=message)
	return response

def main():
	parser = argparse.ArgumentParser(description="Test Slack API integration.")
	parser.add_argument("user", metavar="user", type=str, nargs=1)
	parser.add_argument("message", metavar="message", type=str, nargs=1)
	args = parser.parse_args()
	if not args.user[0].startswith('@'):
		args.user[0] = '@' + args.user[0]
	client = WebClient(token=SLACK_TOKEN)
	print(send_message(client, args.user[0], args.message[0]))



if __name__ == "__main__":
	main()
