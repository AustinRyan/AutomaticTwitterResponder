import tweepy
import time
from keys import *
print("This is my twitter bot", flush = True)



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

    #Using the .keys and mentions[0] will return first mention and only the keys or variables that is returned
    #print(mentions[0].__dict__.keys()) 


FILE_NAME = 'last_seen_id.txt'

#following methods will get the last id seen, and if the id is the same it will not tweet back at the user
#It will store the last seen ID in a seperate file called last_seen_id.txt
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush = True)
    last_seen_id = retireve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

#Reverse the for loop to get the first mentions first

for mention in reversed(mentions):
    print(str(mention.id) + ' - ' + mention.full_text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#helloworld' in mention.full_text.lower(): #if any of the mentions include 'helloworld' convert to lowercase
        print('found #helloworld')
        print('respond back...')
        api.update_status('@' + mention.user.screen_name + 'yo dawg', mention.id) #if theres a hashtag hellow world, the code will automatically respond to that user that tagged you with helloworld


while True:
    reply_to_tweets()
    time.sleep(2)





 