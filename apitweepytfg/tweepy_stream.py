from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from apitweepytfg import twitter_creds


class TwitterStreamer:
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, hash_tag_list, maxTweets):

        auth = OAuthHandler(twitter_creds.CONSUMER_KEY, twitter_creds.CONSUMER_SECRET)
        auth.set_access_token(twitter_creds.ACCESS_TOKEN, twitter_creds.ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                         retry_errors=5)

        statuses = []
        streamListener = StdOutListener()
        stream = Stream(auth=api.auth, listener=streamListener)

        maxTweets = int(maxTweets)
        ob = tweepy.Cursor(api.search, q=hash_tag_list, rpp=100, count=20, result_type="recent", include_entities=True, lang="es").items(maxTweets)
        for tweet in ob:
            statuses += [tweet.text]
        print(statuses)
        return statuses


class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """



    def on_status(self, status):
        print(status.text)


    def on_error(self, status):
        print(status)
