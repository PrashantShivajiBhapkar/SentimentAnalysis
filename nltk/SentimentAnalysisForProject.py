import nltk
import getTweets as twt
from nltk.corpus import stopwords as stpWrds
from nltk.tokenize import word_tokenize
import json
import os
import string


def preProcess(listOfTexts, topN=50):
    """Accepts a list of texts and writes a json file containin frequencies of topN
    words in the list of texts"""
    stopwords = set(stpWrds.words('english'))
    allWords = []
    topN_dict = {}
    for tweet in listOfTexts:
        words = word_tokenize(tweet)
        allWords.extend(word.lower() for word in words if word.lower() not in stopwords
                        and word not in string.punctuation and word not in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})

    # Get the frequency distribution of each word
    fdist = nltk.FreqDist(allWords)  # type = <class 'nltk.probability.FreqDist'>.

    # Store words and corresponding frequencies in dictionary
    # fdist.most_common(topN) returns list of tuples (value1=term, value2=count)
    for val in fdist.most_common(topN):
        topN_dict[val[0]] = str(val[1])

    # Dump the dictionary into a JSON file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/wordCloudData.json', 'w') as fp:
        json.dump(topN_dict, fp)


# For debugging
if __name__ == '__main__':
    a = twt.GetTweets()
    tweets = a.getTweetByKeyword('Trump', 0, 10000)
    # print(tweets)
    # print(type(tweets))
    print(len(tweets))
    for i in tweets:
        print(i)

    # print(tweets[0].decode('unicode_escape').encode('ascii', 'ignore'))
    # Need to save as JSON
    preProcess(tweets, 100)
    # print(tweets[0])
# tweets contain a lot of garbage. Need cleaning
