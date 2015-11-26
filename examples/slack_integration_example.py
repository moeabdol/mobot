#!/usr/local/bin/python2
import sys
sys.path.append("../")
import time
from slackclient import SlackClient
from utils import read_slack_access_token
from utils import get_channel_id

channel = "#general"
token = read_slack_access_token("../slack_access_token.txt")
sc = SlackClient(token)
channel_id = get_channel_id(sc, channel)

if sc.rtm_connect():
  while True:
    events = sc.rtm_read()
    for event in events:
      print event
    time.sleep(1)
else:
  print "Connection to Slack RTM API failed"
