# Mobot
Mobot is an [AIML](https://en.wikipedia.org/wiki/AIML) chatbot for
[Slack](https://slack.com/). You can customize **mobot** to work in your Slack
team.

## Dependencies
You can Install the following dependencies using pip or easy_install
* [PyAIML](https://github.com/creatorrr/pyAIML) Python AIML Interpreter
* [SlackClient](https://github.com/slackhq/python-slackclient) Slack API wrapper
```
$ pip install aiml
$ pip install slackclient
```

## How To
First make sure you rename api_keys_example.txt file to api_keys.txt. Get your
[Slack API token](https://api.slack.com/web) and paste it in the file.
```
slack_api_key = "xoxp-1111111111-22222222222-33333333333-4444444444"
```

#### Customize Mobot's Predicates
In **utils.py** under the **configure_chatbot()** method you can customize all
of the chatbot's predictates; such as, name, age, favorite sport team, etc.
```python
kernel.setBotPredicate("name"       , "mobot")
kernel.setBotPredicate("age"        , "25")
kernel.setBotPredicate("birthday"   , "Nov. 23, 1995")
kernel.setBotPredicate("birthplace" , "Cairo, Egypt")
```

#### Customize Mobot's Personality
All files in the **aiml** directory make up mobot's personality. You can go
through these files one by one and modify specific responses that you want mobot
to provide. All aiml files are part of [Alice](http://www.alicebot.org/)
standard aaa us-english aiml files which you can download [here](http://code.google.com/p/aiml-en-us-foundation-alice/downloads/detail?name=aiml-en-us-foundation-alice.zip)

## Run
```
$ python chatbot.py                   # will join all channels
$ python chatbot.py -j general        # will join general channel only
$ python chatbot.py -j general random # will join general and random channels
```

## Notes
1. Mobot will only respond back to users addressing it directly as **@mobot**.
2. Mobit will greet new users joining channels.
* You can further extend mobot to do different things when different events
  happen.
