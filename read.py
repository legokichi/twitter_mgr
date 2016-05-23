# coding: utf-8

import json
import tweepy

def read_json_file(file_name):
    with open(file_name) as f:
        jso = json.loads(f.read(), "utf-8")
        return jso

def get_api(jso):
    print "jso", jso
    auth = tweepy.OAuthHandler(jso["CONSUMER_KEY"], jso["CONSUMER_SECRET"])
    auth.set_access_token(jso["ACCESS_TOKEN"], jso["ACCESS_SECRET"])
    print "auth", auth
    api = tweepy.API(auth)
    print "api", api
    return api

obj = read_json_file("./key_dxcknd.json")
api = get_api(obj)
user_timeline = api.user_timeline(obj["OWNER"])
print type(user_timeline)
status = user_timeline[0]
user = status.author
print user.name, user.screen_name, status.text
print "ok"
