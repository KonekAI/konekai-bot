import os
from pathlib import Path
from dotenv import load_dotenv
import uuid

from slackeventsapi import SlackEventAdapter
import slack_sdk

from flask import Flask, request, Response
import openAPI as ai 
#####################################################################
#setup web server
app = Flask(__name__)

# load slack tokens from the .env file
load_dotenv(dotenv_path = Path('.') / '.env')
#setup webClient 
client = slack_sdk.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
# slack_events_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events', app)

#####################################################################
# Support funcitons 

BOT_ID = client.api_call("auth.test")['user_id']

def answerFormat(question, answer):
    return [{
        'type': 'section',
        'text': {
            'type':'mrkdwn',
             'text': (
                f'*Q:* {question} \n\n'
                f'*A:* {answer}'
                )
            }
    }]

#####################################################################
# authorization
@app.route("/oauthButton", methods=["GET"])
def oAuth_generateButton():
    client_id = os.environ["SLACK_BOT_CLIENT_ID"]
    state = uuid.uuid1()
    os.putenv("TEMP_STATE", f"{state}")
    return f'<a href="https://slack.com/oauth/v2/authorize?scope=channels:read,groups:read,channels:manage,chat:write&client_id={ client_id }&state={ state }"><img alt=""Add to Slack"" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>'


   
@app.route("/oauthRedirect", methods=["POST","GET"])
def oAuth_exchange():
    receivedState = request.args['state']
    auth_code = request.args['code']
    if(os.environ["TEMP_STATE"]) == receivedState:
        # get auth tokens from Slack
        response = client.oauth_v2_access(
            client_id=client_id,
            client_secret=client_secret,
            code=auth_code
        )
    else:
        return "Invalid State"


    os.environ["SLACK_BOT_TOKEN"] = response['access_token']

    return "Auth complete!"
    

#####################################################################
# COMMANDS
@app.route('/ai-qna', methods=['POST'])
def qna():
    payload = request.form
    user_id = payload.get('user_id')
    # channel_id = payload.get('channel_id')
    text = payload.get('text')

    # check if the text is empty
    if text == '':
        client.chat_postMessage(channel=user_id, 
                                text= "You did not ask me a queston. You can write your question after the command, for example (/ai-qna when did TOHack first began?)" 
                                )
    else:        
        # pass text to the AI funciton
        ans = ai.puppyTest()[0]
        # ans = ai.askOpenAI(text)[0]
        client.chat_postMessage(channel=user_id, 
                                text= text, 
                                blocks = answerFormat(question = text, answer = ans)
                                )
        
    return Response(), 200

#####################################################################
