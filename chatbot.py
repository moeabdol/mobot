#!/usr/local/bin/python2

import aiml
import time
from utils import connect_to_slack_rtm_api
from utils import get_channel_id
from utils import configure_chatbot
from utils import get_username
from utils import is_message_to_chatbot
from utils import drop_botname_from_message

channel = "#ai"
connected, sc = connect_to_slack_rtm_api("slack_access_token.txt")
channel_id = get_channel_id(sc, channel)

if connected:
  kernel = aiml.Kernel()
  kernel.learn("std-startup.xml")
  kernel.respond("load aiml b")
  configure_chatbot(kernel)

  while True:
    events = sc.rtm_read()
    if events:
      for event in events:
        try:
          if event["channel"] == channel_id:
            message = event["text"]
            user_id = event["user"]
            username = get_username(sc, user_id)
            if is_message_to_chatbot(kernel, message):
              message = drop_botname_from_message(kernel, message)
              sc.rtm_send_message(channel_id, "@" + username + ": " +
                                  kernel.respond(message))
        except:
          pass
    time.sleep(1)
else:
  print "Connection to Slack RTM API Failed"
