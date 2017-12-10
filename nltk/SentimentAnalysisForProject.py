import nltk
import getTweets as twt
from nltk.corpus import stopwords as stpWrds
from nltk.tokenize import word_tokenize
import json
import os
import string
import re


def wordCloud(text, topN=50, lang='english'):
    """This function accepts a text in language-lang and returns a dict of topN
       tokens. dictFormat - {<token>: <frequency>}
       PARAMS: text(string) - string to get topN most occurring tokens from
               topN(int) - count of most occurring tokens
               lang(string) - language of the text
       RETURNS: dict of tokens after filtration"""
    topN_dict = {}
    # Get list of filtered tokens
    stopWrdsFilteredTknLst = filterStopWords(text, lang)
    # Get the frequency distribution of each word
    fdist = nltk.FreqDist(stopWrdsFilteredTknLst)
    # type(fdist) type=<class 'nltk.probability.FreqDist'>

    # Store words and corresponding frequencies in dictionary
    # fdist.most_common(topN) returns list of tuples->value1=term, value2=count
    for val in fdist.most_common(topN):
        topN_dict[val[0]] = str(val[1])
    print(extractPOS(text, pos='noun'))
    return topN_dict


def filterStopWords(text, lang='english'):
    """PARAMS: text(string) - string to remove stopwords from
               lang(string) - language of text
       RETURNS: list of tokens after filtration
    """
    stopwords = set(stpWrds.words(lang))
    tokensLst = word_tokenize(text)
    filteredTokenLst = []
    filteredTokenLst.extend(word.lower() for word in tokensLst if word.lower()
        not in stopwords and word not in string.punctuation and word not in {'0','1','2','3','4','5','6','7','8','9'})
    return filteredTokenLst


def extractPOS(text, pos, lang='english'):
    """PARAMS: text(string) - string to extract tokens having a particular POS from
               pos(string) - Part of speech: Noun, Adjective, Verb etc.
       RETURNS(list): - list of tokens having parametered pos
    """
    filteredTokens = filterStopWords(text, lang)
    taggedWordsLst = nltk.pos_tag(filteredTokens)
    taggedWordsDict = {}
    tknsWithPOSLst = []
    for tup in taggedWordsLst:
        if tup[1] not in taggedWordsDict.keys():
            taggedWordsDict[tup[1]] = [tup[0]]
        else:
            taggedWordsDict[tup[1]].append(tup[0])
    if pos.lower() == 'noun':
        reObj = re.compile('^NN.?')
        for key in taggedWordsDict.keys():
            if reObj.match(key):
                print(key)
                tknsWithPOSLst.extend(taggedWordsDict[key])
    elif pos.lower() == 'adjective':
        reObj = re.compile('^JJ.?')
        for key in taggedWordsDict.keys():
            if reObj.match(key):
                print(key)
                tknsWithPOSLst.extend(taggedWordsDict[key])
    elif pos.lower() == 'verb':
        reObj = re.compile('^VB.?')
        for key in taggedWordsDict.keys():
            if reObj.match(key):
                print(key)
                tknsWithPOSLst.extend(taggedWordsDict[key])

    print(taggedWordsDict)
    return tknsWithPOSLst


def writeJson(dictToWrite):
    # Dump the dictionary into a JSON file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/wordCloudData' + '' + '.json', 'w') as fp:
        json.dump(dictToWrite, fp)


# For debugging
if __name__ == '__main__':
    # a = twt.GetTweets()
    # tweets = a.getTweetByKeyword('Trump', 0, 10000)
    # print(tweets)
    # print(type(tweets))
    # print(len(tweets))
    # for i in tweets:
    #     print(i)
    a = 'Apple Inc. is an American multinational technology company headquartered in Cupertino, California that designs, develops, and sells consumer electronics, computer software, and online services. The company\'s hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple Watch smartwatch, the Apple TV digital media player, and the HomePod smart speaker.'
    # print(tweets[0].decode('unicode_escape').encode('ascii', 'ignore'))
    # Need to save as JSON
    print(wordCloud(a, 10))
    # print(tweets[0])
# tweets contain a lot of garbage. Need cleaning
