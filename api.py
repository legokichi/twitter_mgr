# coding: utf-8
import sys
sys.path.append('../tweepy')
import json
import tweepy
import csv

def read_json_file(file_name):
    with open(file_name) as f:
        jso = json.loads(f.read(), "utf-8")
        return jso

def get_api(jso):
    #print "jso", jso
    auth = tweepy.OAuthHandler(jso["CONSUMER_KEY"], jso["CONSUMER_SECRET"])
    auth.set_access_token(jso["ACCESS_TOKEN"], jso["ACCESS_SECRET"])
    #print "auth", auth
    api = tweepy.API(auth)
    #print "api", api
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

def read_tsv_file(filename):
    results = []
    with open(filename,'rb') as fp:
        tsv = csv.reader(fp, delimiter='\t')
        for row in tsv:
            if 0 < len(row):
                results.append(tuple(row))
    return results

