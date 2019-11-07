import tweepy
import urllib.request
import os
import time

#OAuth 
consumer_key = "kyvLPXspnLrHBZ6irmKGzuuLx"
consumer_secret = "Z51dQfTlUC5H9x56EYvTtfxPwrBWmOcWdcM5m3rpWoor9MftWc"
access_token = "741953756653309952-u8PmzBRyLPqPYxRJrMeDTZTwusPtagt"
access_token_secret = "afXYe1AB4sGRhtJumZO5Yr6hbRVbUKy51Dwo5jXFIRDFm"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



user_handle = "GreatPornPix"
num_tweets = 50
folder = "C:\\Users\\Tjorven\\Desktop\\DL_Test"



def download(user_handle, amount, folder):
    timeline = tweepy.Cursor(api.user_timeline,
                            id = user_handle,
                            include_rts = False, exclude_Replies = True).items(amount)


    input("start download?")
    i = 1
    
    try:
        for tweet in timeline:
            if "media" in tweet.entities:
                dest  = folder + "\\pic" + str(i) + ".png"
                for image in tweet.entities["media"]:
                    urllib.request.urlretrieve(image["media_url"], dest)
                    i += 1
    except tweepy.TweepError:
        print("An Error has occured")
    print("Return_rate = " + str(round((i - 1) / num_tweets * 100,2)) + "%")



def clear_folder(folder):
    input("delete folder contents now?")
    for file in os.listdir(folder):
        os.unlink(folder + "\\"  + file)


def run(user_handle, amount, folder):

    download(user_handle, num_tweets, folder)
    clear_folder(folder)


run(user_handle, num_tweets, folder)