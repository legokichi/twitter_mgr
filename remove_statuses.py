# coding: utf-8
import sys
sys.path.append('../tweepy')
import tweepy
import csv
from api import *

def remove_status(author, id):
    if author != "dxcknd":
        print "unretweet", author, id
        status = api.unretweet(id)
    else:
        print "destroy_status", author, id
        status = api.destroy_status(id)
    return status

obj = read_json_file("./key_dxcknd.json")
api = get_api(obj)
dels = read_tsv_file("del.tsv")
for _del in dels:
    id = _del[0]
    author = _del[2]
    try:
        status = remove_status(author, id)
    except tweepy.error.TweepError as err:
        print err
    #showRecur(status)
    
print "ok"


