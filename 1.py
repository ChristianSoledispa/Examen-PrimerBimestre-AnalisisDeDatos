Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################

#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://ChristianSoledispa:soledispa1@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('tokyo2020')
except:
    db = server['tokyo2020']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[11.4037,41.7901,13.9414,43.568])  
twitterStream.filter(track=['tokyo2020','juegos_olimpicos'])
