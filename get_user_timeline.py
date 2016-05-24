# coding: utf-8
import sys
sys.path.append('../tweepy')
import tweepy
from api import *

obj = read_json_file("./key_dxcknd.json")
api = get_api(obj)

for status in limit_handled(tweepy.Cursor(api.user_timeline, obj["OWNER"]).items()):
    if  hasattr(status, 'retweeted_status'):
        status = status.retweeted_status
    #showRecur(status)
    user = status.author
    line = str(status.id)+"\t"+user.name+"\t"+user.screen_name+"\t"+removeCRLF(status.text)
    print line.encode('utf-8')

print "ok"


