import tweepy as tw


class GetTweets():
    def __init__(self, consumer_key, consumer_secret, access_token, access_tkn_secret):
        self._auth = tw.OAuthHandler(consumer_key, consumer_secret)
        self._auth.set_access_token(access_token, access_tkn_secret)
        self._twitter = tw.API(self._auth)

    def getTweetByKeyword(self, searchKeyword, hashtagFlag=0, volume=100):
        """Returns a list of tweets of s per the search keyword"""
        public_tweets = self._twitter.search(
            ((hashtagFlag and '#' or '') + searchKeyword), count=volume)
        l = []
        for tweet in public_tweets:
            l.append(tweet.text.encode("utf-8"))
        return l


if __name__ == '__main__':
    consumer_key = 'sSRGLaVYyWgtU4hVP5cJGmgmB'
    consumer_secret = 'EY438AALpE8uixPx5HubQhojNzUbaWgY9CRGkWBb5uFVLgNAeT'
    access_token = '159740497-y5MiYlkJUlopvVj8ziMPqZE7s1ovTMp4tfsOq7V0'
    access_tkn_secret = 'Waz6c3kls3ueOQ78aVAoC0o6kwmh1rWLRzK5DsnJlP05I'
    tweet = GetTweets(consumer_key, consumer_secret, access_token, access_tkn_secret)
    l = tweet.getTweetByKeyword('Obama', 1)
    for i in l:
        print(i)
