import nltk
import getTweets as twt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preProcess(listOfTweets, topN=50):
    stpwords = set(stopwords.words('english'))
    tweets = []
    for tweet in listOfTweets:
        words = word_tokenize(str(tweet))
        tweets.extend(word for word in words if word not in stpwords)

    fdist = nltk.FreqDist(tweets)
    return(fdist.most_common(topN))


if __name__ == '__main__':
    a = twt.GetTweets()
    tweets = a.getTweetByKeyword('Trump', 1, 1000)
    # print(tweets[0])
    # print(tweets[0].decode('unicode_escape').encode('ascii', 'ignore'))
    print(preProcess(tweets, 100))
    # print(tweets[0])
# tweets contain a lot of garbage. Need cleaning
