from urllib2 import urlopen, URLError
import datetime as dt
from pymongo import MongoClient

TEAM_NAME = "hacknode1"

def get_collection():
    return MongoClient()[TEAM_NAME].articles 

def top_articles():
    coll = get_collection()
    articles = coll.find()
    return list(articles)

def insert_article(article):
    coll = get_collection()
    article["score"] = 0
    article["date"] = dt.datetime.now()
    print "Inserting ->", article
    coll.insert(article)
    return True

#use below as template for $inc feature
def track_click(url):
    coll = get_collection()
    print "Tracking ->", url
    coll.update({"link": url}, 
                {"$inc": 
                    {"score": 1}
                })
    return True


#below necessary database features
def add_marker(address):
	pass
	
def get_parent:
	pass
	
def get_children:
	pass
	
def update_branch_count:
	pass
	
def update_markers:
	pass
	

def 


#validation
def validate_submission(params):
    errors = {}
    def err(id, msg):
        errors[id] = msg
    title = params["title"]
    title = title.strip()
    if len(title) < 2:
        err("title", "title must be > 2 characters")
    if len(title) > 150:
        err("title", "title may not be > 150 characters")
    link = params["link"]
    link = link.strip()
    try:
        opened = urlopen(link)
        link = opened.geturl()
    except (URLError, ValueError):
        err("link", "link could not be reached")
    if len(errors) > 0:
        return (False, errors)
    else:
        return (True, errors)
