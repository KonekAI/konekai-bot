import slack_sdk
import os
from pathlib import Path
from dotenv import load_dotenv

from flask import Flask, request, Response
# from slackeventsapi import SlackEventAdapter

#####################################################################
#setup web server
app = Flask(__name__)

# load slack tokens from the .env file
load_dotenv(dotenv_path = Path('.') / '.env')
#setup webClient 
client = slack_sdk.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
#####################################################################
# Test
# client.chat_postMessage(channel='general', text="Hello World!", icon_emoji=":robot:")


#####################################################################
# COMMANDS
@app.route('/ai-qna', methods=['POST'])
def message_count():
    request = request.form

    user_id = request.get('user_id')
    channel_id = request.get('channel_id')
    text = data.get('text')
    # get the value from message_counts[user_id], if the user_id does not exist, return 0  
    count = message_counts.get(user_id, 0)

    client.chat_postMessage(channel=user_id, text= "check")
    return Response(), 200