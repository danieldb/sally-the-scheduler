from copyreg import constructor
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
import datetime

from Schedule import Schedule
from ScheduleEvent import ScheduleEvent

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET_'], "/slack/events", app)

client = slack.WebClient(token= os.environ['SLACK_TOKEN_'])
BOT_ID = client.api_call("auth.test")["user_id"]
client.chat_postMessage(channel="#schedule", text="Started Scheduling...")

shed = Schedule(client)


@slack_event_adapter.on('message')
def message(payload):
  event = payload.get('event', {}) 
  channel_id = event.get('channel')
  user_id = event.get('user')
  text = event.get('text')
  print('test')

  if (user_id == BOT_ID): return
  args = text.split(' ')
  if (args[0] == '!add'):
    print(args)
    se = ScheduleEvent(args[1], args[2], args[3] == "AM", args[4])
    print(se.name, se.date)
    shed.add(se)
  if (args[0] == '!remove'):
    shed.remove(args[1])
  if(args[0] == '!next'):
    shed.next()
  if(args[0] == '!fetch'):
    shed.fetch()

if __name__ == '__main__':
  app.run(debug=True, port=3000)