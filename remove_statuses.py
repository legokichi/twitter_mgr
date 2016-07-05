# coding: utf-8
import sys
sys.path.append('../tweepy')
import tweepy
import csv
from api import *
param = sys.argv

if len(param) != 3:
    print """
Example:

    python find_author.py key_dxcknd.json del.tsv

    """
    exit()


def remove_status(author, id, myname):
    if author != myname:
        print "unretweet", author, id
        status = api.unretweet(id)
    else:
        print "destroy_status", author, id
        status = api.destroy_status(id)
    return status


obj = read_json_file(param[1])
api = get_api(obj)
dels = read_tsv_file(param[2])
for _del in dels:
    id = _del[0]
    author = _del[2]
    try:
        status = remove_status(author, id, obj["OWNER"])
    except tweepy.error.TweepError as err:
        print err
    #showRecur(status)
    
print "\n"


