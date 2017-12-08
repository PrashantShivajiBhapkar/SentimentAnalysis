from bs4 import BeautifulSoup
import urllib3


def scraper(url):
    http = urllib3.PoolManager()
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data, 'lxml')
    # html = soup.prettify()
    # print(soup.prettify())
    # paragraphs = []
    allText = ''
    for string in soup.stripped_strings:
        allText += '' + string
    print(allText)


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Donald_Trump"
    url2 = 'http://www.cnn.com/2017/12/08/politics/george-papadopoulos-fiancee/index.html'
    url3 = 'https://economictimes.indiatimes.com/news/company/corporate-trends/the-rise-and-stunning-fall-of-unitech/articleshow/61990781.cms'
    scraper(url2)
