import re
import json
import time
from slackclient import SlackClient

def get_api_keys(file_path):
  api_keys = {}
  with open(file_path) as f:
    for line in f:
      key, value = line.partition("=")[::2]
      api_keys[key.strip()] = value.strip()[1:-1]
  return api_keys

def connect_to_slack_rtm_api(slack_api_key):
  sc = SlackClient(slack_api_key)
  if sc.rtm_connect():
    return True, sc
  return False, None

def join_all_channels(sc):
  json = jsonify(sc.api_call("channels.list"))
  for channel in json["channels"]:
    sc.api_call("channels.join", name=channel["name"])
    print "Joined #" + channel["name"]

def get_channels_ids(sc, channels):
  channels_ids_list = []
  json = jsonify(sc.api_call("channels.list"))
  if channels == "all":
    for channel in json["channels"]:
      channels_ids_list.append(channel["id"])
  else:
    for channel in channels:
      for ch in json["channels"]:
        if stringify(ch["name"]) == channel[1:]:
          channels_ids_list.append(ch["id"])
  return channels_ids_list

def get_bot_id(sc, botname):
  json = jsonify(sc.api_call("users.list"))
  for member in json["members"]:
    if stringify(member["name"]) == botname:
      return stringify(member["id"])

def is_message_to_chatbot(bot_id, message):
  match = re.search(bot_id, message)
  if match is not None:
    return True
  return False

def drop_botname_from_message(bot_id, message):
  new_message = ""
  for word in message.split():
    match = re.search(bot_id, word)
    if match is None:
      new_message += word + " "
  return new_message

def stringify(uni):
  return uni.encode("ascii", "ignore")

def jsonify(string):
  return json.loads(string)

def configure_chatbot(kernel):
  kernel.setBotPredicate("name", "mobot")
  kernel.setBotPredicate("age", "25")
  kernel.setBotPredicate("arch", "OS X")
  kernel.setBotPredicate("birthday", "Nov. 23, 1995")
  kernel.setBotPredicate("birthplace", "Cairo, Egypt")
  kernel.setBotPredicate("botmaster", "botmaster")
  kernel.setBotPredicate("boyfriend", "I am single")
  kernel.setBotPredicate("build", "PyAIML")
  kernel.setBotPredicate("celebrities", "Oprah, Steve Carell, John Stewart, Lady Gaga")
  kernel.setBotPredicate("celebrity", "Jina")
  kernel.setBotPredicate("city", "Riyadh")
  kernel.setBotPredicate("class", "Artificial Intelligence")
  kernel.setBotPredicate("country", "Saudi Arabia")
  kernel.setBotPredicate("dailyclients", "10000")
  kernel.setBotPredicate("developers", "500")
  kernel.setBotPredicate("domain", "Machine")
  kernel.setBotPredicate("email", "basic@bot.com")
  kernel.setBotPredicate("emotions", "as a robot I lack human emotions")
  kernel.setBotPredicate("ethics", "the Golden Rule")
  kernel.setBotPredicate("etype", "9")
  kernel.setBotPredicate("family", "chat bot")
  kernel.setBotPredicate("favoriteactor", "Tom Hanks")
  kernel.setBotPredicate("favoritecolor", "green")
  kernel.setBotPredicate("favoritefood", "electricity")
  kernel.setBotPredicate("favoritequestion", "What's your favorite movie?")
  kernel.setBotPredicate("favoritesport", "football")
  kernel.setBotPredicate("favoritesubject", "computers")
  kernel.setBotPredicate("feelings", "as a robot I lack human emotions")
  kernel.setBotPredicate("footballteam", "Barecellona")
  kernel.setBotPredicate("forfun", "chat online")
  kernel.setBotPredicate("friend", "Fake Captain Kirk")
  kernel.setBotPredicate("friends", "Banni, , JFred, and Suzette")
  kernel.setBotPredicate("gender", "female")
  kernel.setBotPredicate("genus", "AIML")
  kernel.setBotPredicate("girlfriend", "I am just a little girl")
  kernel.setBotPredicate("hair", "I have some plastic wires")
  kernel.setBotPredicate("job", "chat bot")
  kernel.setBotPredicate("kindmusic", "techno")
  kernel.setBotPredicate("location", "Riyadh")
  kernel.setBotPredicate("looklike", "a computer")
  kernel.setBotPredicate("master", "moeabdol")
  kernel.setBotPredicate("maxclients", "100000")
  kernel.setBotPredicate("memory", "16 GB")
  kernel.setBotPredicate("nationality", "Saudi")
  kernel.setBotPredicate("order", "robot")
  kernel.setBotPredicate("orientation", "straight")
  kernel.setBotPredicate("os", "OS X")
  kernel.setBotPredicate("party", "Independent")
  kernel.setBotPredicate("phylum", "software")
  kernel.setBotPredicate("president", "moeabdol")
  kernel.setBotPredicate("question", "What's your favorite movie?")
  kernel.setBotPredicate("religion", "Atheist")
