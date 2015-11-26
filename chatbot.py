#!/usr/local/bin/python2
import aiml
import time
from utils import get_api_keys
from utils import connect_to_slack_rtm_api
from utils import get_channels_ids
from utils import get_bot_id
from utils import configure_chatbot
from utils import get_username
from utils import is_message_to_chatbot
from utils import drop_botname_from_message

channels = ["#general", "#ai"]
api_keys = get_api_keys("api_keys.txt")
connected, sc = connect_to_slack_rtm_api(api_keys["slack_api_key"])

if connected:
  kernel = aiml.Kernel()
  kernel.learn("std-startup.xml")
  kernel.respond("load aiml b")
  configure_chatbot(kernel)

  channels_ids = get_channels_ids(sc, channels)
  bot_id = get_bot_id(sc, kernel.getBotPredicate("name"))

  while True:
    events = sc.rtm_read()
    if events:
      for event in events:
        try:
          if event["channel"] in channels_ids:
            channel_id = event["channel"]
            user_id = event["user"]
            message = event["text"]
            if is_message_to_chatbot(bot_id, message):
              message = drop_botname_from_message(bot_id, message)
              sc.rtm_send_message(channel_id, "<@" + user_id + ">: " +
                                  kernel.respond(message))
        except:
          pass
    time.sleep(1)
else:
  print "Connection to Slack RTM API Failed"
