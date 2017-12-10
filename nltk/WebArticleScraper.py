from bs4 import BeautifulSoup
import urllib3
from collections import OrderedDict
import SentimentAnalysisForProject as safp


def scraper(url, sourceTagDict):
    """ params: url of the webpage from which text needs to be fetched.
        sourceTagDict: dict of tags as keys with values of format
        {attribute: value}.
        ex: <p class='xxx'> -> {'p': {"class" : 'zn-body__paragraph'}}
        sourceTagDict contains tags that contain the main text content
        of the article.
        returns: a tuple (title, newsContent)
    """
    http = urllib3.PoolManager()
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data, 'lxml')
    title = soup.title.get_text()
    newsContent = ''
    for (keyTag, attrVals) in sourceTagDict.items():
        for tag in soup.find_all(keyTag, attrVals):
            newsContent += ' ' + tag.get_text()
    return (title, newsContent)


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Donald_Trump"
    url2 = 'http://www.cnn.com/2017/12/08/politics/george-papadopoulos-fiancee/index.html'
    url3 = 'https://economictimes.indiatimes.com/news/company/corporate-trends/the-rise-and-stunning-fall-of-unitech/articleshow/61990781.cms'
    url4 = 'http://www.cnn.com/2017/12/09/middleeast/iraq-isis-military-liberated/index.html'

    cnnUrl1 = 'http://www.cnn.com/2017/12/09/politics/alex-kozinksi-accusations/index.html'
    cnnUrl2 = 'http://www.cnn.com/2017/12/09/politics/donald-trump-rigged-sick-institutions/index.html'
    cnnUrl3 = 'http://www.cnn.com/2017/12/09/politics/trump-pensacola-speech-analysis/index.html'
    cnnUrl4 = 'http://www.cnn.com/2017/12/09/politics/conyers-special-election-dates/index.html'
    cnnUrl5 = 'http://www.cnn.com/2017/12/08/politics/trent-franks-surrogacy-accuser/index.html'
    urlList = [cnnUrl1, cnnUrl2, cnnUrl3, cnnUrl4, cnnUrl5]
    cnnTagDict = OrderedDict()
    cnnTagDict = {'p': {"class": 'zn-body__paragraph'}, 'div': {"class": 'zn-body__paragraph'}}
    newsStories = {}
    allNews = ''
    for url in urlList:
        title, newsContent = scraper(url, cnnTagDict)
        newsStories[title] = newsContent
        allNews += newsContent
    print(newsStories['Appeals judge facing claims of inappropriate sexual conduct - CNNPolitics'])
    # _, content = scraper(cnnUrl1, cnnTagDict)

    safp.writeJson(safp.wordCloud(allNews, topN=100, pos='adjective'))
    cnnLanding = 'http://www.cnn.com/'
