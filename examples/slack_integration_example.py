#!/usr/local/bin/python2
import sys
sys.path.append("./")
sys.path.append("../")
import time
from slackclient import SlackClient
from utils import get_api_keys

channel = ["#general"]
api_keys = get_api_keys("api_keys.txt")
sc = SlackClient(api_keys["slack_api_key"])

if sc.rtm_connect():
  while True:
    events = sc.rtm_read()
    for event in events:
      print event
    time.sleep(1)
else:
  print "Connection to Slack RTM API failed"
