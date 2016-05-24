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


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def showRecur(obj, i=2):
    if i == 0: return
    for prop, val in vars(obj).iteritems():
        if(not hasattr(val, '__dict__')):
            print prop, ": ", val
        else:
            print prop, ">>>"
            showRecur(val,i-1)
            print "<<<", prop

def removeCRLF(text):
    return text.replace('\n', ' ').replace('\r', '')


obj = read_json_file("./key_dxcknd.json")
api = get_api(obj)

for status in limit_handled(tweepy.Cursor(api.user_timeline, obj["OWNER"]).items(10)):
    if  hasattr(status, 'retweeted_status'):
        status = status.retweeted_status
    #showRecur(status)
    user = status.author
    print str(status.id)+"\t"+user.name+"\t"+user.screen_name+"\t"+removeCRLF(status.text)

print "ok"


