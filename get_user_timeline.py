# coding: utf-8
import sys
sys.path.append('../tweepy')
import tweepy
from api import *

param = sys.argv

if len(param) != 2:
    print """
Example:

    python get_user_timeline.py key_dxcknd.json >> user/log_.tsv
"""
    exit()

obj = read_json_file(param[1])
api = get_api(obj)

for status in limit_handled(tweepy.Cursor(api.user_timeline, obj["OWNER"]).items()):
    if  hasattr(status, 'retweeted_status'):
        status = status.retweeted_status
    #showRecur(status)
    user = status.author
    line = str(status.id)+"\t"+user.name+"\t"+user.screen_name+"\t"+removeCRLF(status.text)
    print line.encode('utf-8')

print "\n"


