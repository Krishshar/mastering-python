# open several google search results

import webbrowser
import requests
import sys
import bs4

BASE_URL = 'http://google.com/search?q='

if __name__ == '__main__':
    # display text while downloading the Google page.
    print("Googling....")
    res = requests.get(BASE_URL + ' '.join(sys.argv[1:]))

    # retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # open a browser tab for each result
    link_elems = soup.select('.r a')
    num = min(5, len(link_elems))
    for i in range(num):
        webbrowser.open('https://www.google.com' + link_elems[i].get('href'))
