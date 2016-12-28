#goodreadrecs.py
import configparser
import os
import time
import goodreads
from goodreads import client

gc = None
clientAuthenticated = False
recent_reviews = []
reviews_per_user = {}
rev_per_user_done = False

def initiate_goodreads_lient():
    global gc
    #read api connection details from ini file.
    config = configparser.ConfigParser()
    #os.path.dirname(os.path.realpath(__file__))
    config.read(os.path.curdir+r'\goodreads.ini')
    print(str(config.sections()))
    api_key = config.get('access_info', 'api_key')
    api_secret = config.get('access_info', 'api_secret')
    gc = client.GoodreadsClient(api_key,api_secret)
    return gc

def authenticate_goodreads_client():
    global gc
    try:
        gc.authenticate()
    except Exception as e:
        print(e.message)
        return False
    return True

def get_goodreads_recent_reviews():
    global recent_reviews
    if not recent_reviews:
        print('recent_reviews not retrieved before')
        if gc is None:
            print('goodreads client not initiated')
            initiateGoodReadsClient()
        print('Retrieving recent_reviews..')
        recent_reviews = gc.recent_reviews()
        time.sleep(2)
    return recent_reviews

        



    
