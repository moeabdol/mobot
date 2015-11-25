import utils
import time
from slackclient import SlackClient

channel = "#ai"

token = utils.read_slack_access_token("slack_access_token.txt")
sc = SlackClient(token)

channel_id = utils.get_channel_id(sc, channel)

if sc.rtm_connect():
  while True:
    events = sc.rtm_read()
    if events:
      for event in events:
        if "channel" in event.keys() and "type" in event.keys():
          if event["channel"] == channel_id and event["type"] == "message":
            message = event["text"]
            user = event["user"]
            print user, message
    time.sleep(1)
else:
  print "Connection to Slack RTM API failed"
