from slack import WebClient
from alfredobot import AlfredoBot
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new NestorBot
alfredo_bot = AlfredoBot("#desarrollo")

# Get the onboarding message payload
message = alfredo_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)
