import aiml
import utils
import time

channel = "#ai"
connected, sc = utils.connect_to_slack_rtm_api("slack_access_token.txt")
channel_id = utils.get_channel_id(sc, channel)

if connected:
  kernel = aiml.Kernel()
  kernel.learn("std-startup.xml")
  kernel.respond("load aiml b")
  utils.configure_chatbot(kernel)

  while True:
    events = sc.rtm_read()
    if events:
      for event in events:
        if "channel" in event.keys() and "type" in event.keys():
          if event["channel"] == channel_id and event["type"] == "message":
            message = event["text"]
            user_id = event["user"]
            username = utils.get_username(sc, user_id)
            # print user_id, username, message
            # sc.api_call("chat.postMessage", as_user="true:", channel=channel_id,
            #             text=kernel.respond("@" + username+ " " + message))
            # sc.rtm_send_message(channel_id, "@" + username + message)
            sc.rtm_send_message(channel_id, "@" + username + " " +
                                kernel.respond(message))

    time.sleep(1)
  # while True:
  #   print kernel.respond(raw_input(">> "))
else:
  print "Connection to Slack RTM API Failed"
