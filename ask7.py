'''παίρνει από το χρήστη σαν είσοδο δύο χρήστες στο twitter,
βρίσκει ποιος από τους δύο χρησιμοποίησε τις περισσότερες λέξεις στα 50 τελευταία του tweets'''
import tweepy 
consumer_key = "7G71qzXhp5C1n6pZg13TI0dyl"
consumer_secret = "6JeAJefTL5GNGkcQKd77CCPayqINDMKdHvcsoTaI1zxOhghhX4"
access_token = "1218938170156421121-wsulDwzCtmP5U4MdcpYDifq5976df5"
access_token_secret = "YwBwLE7DjXQhIfpStd67p31ycWb1XA58AA8POjZdpYqNH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def user_tweets(user):
    
    last_tweets = api.user_timeline(user, count = 50)
    for tweet in last_tweets:
        text = tweet.text.encode('utf-8')
        words=[]
        s = 0
        for words in text:
            s = s+1
    return s     

user1 = input("Please, insert a Twitter username!")
user2 = input("Please, insert a Twitter username!")
print (user1,"has",user_tweets(user1),"words in his last 50 tweets")
print (user2,"has",user_tweets(user2),"words in his last 50 tweets")

max = 0
t1=int(user_tweets(user1))
t2=int(user_tweets(user2))
if (t1>t2):
    max = t1
    print (user1,"has the most words in his last 50 tweets! (",max,")")
elif (t2>t1):
    max = t2
    print (user2,"has the most words in his last 50 tweets! (",max,")")
else: 
    print ("Both users have the same number of words in their last 50 tweets! (",t1,")")