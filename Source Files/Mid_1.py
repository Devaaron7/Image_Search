import bs4 as bs
import urllib.request
import shutil
from urllib.request import Request, urlopen
import requests

def scrape_reddit(term):
    
    req = Request("https://www.reddit.com/r/Images/search?q={}&restrict_sr=1".format(term), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    webpage = urlopen(req).read()

    soup = bs.BeautifulSoup(webpage, "lxml")

    raw_links = []

    jpg_links = []

    for x in soup.find_all("a"):
        raw_links.append(x.get("href"))


    for y in range(0, len(raw_links)):
        if raw_links[y].find(".jpg") > 0:
            jpg_links.append(raw_links[y])

    ## Logic to remove duplicate links
    for c in jpg_links:
        if jpg_links.count(c) == 2:
            jpg_links.remove(c)

    n = 1
    for y in range(0, len(jpg_links)):
        dl = str(jpg_links[y])
        r = requests.get(dl, allow_redirects=True)
        open(r"Source Files\bin\image_{}.jpg".format(n), "wb").write(r.content)
        n += 1


def scrape_bing(term):
    
    req = Request('https://www.bing.com/images/search?sp=-1&ghc=1&pq=' + term + '&sc=8-5&cvid=DE72170968E34CAD96EB4DDD1601C91B&q=' + term + '&qft=+filterui:imagesize-large&form=IRFLTR&first=1&scenario=ImageBasicHover', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    webpage = urlopen(req).read()

    soup = bs.BeautifulSoup(webpage, "lxml")


    raw_links = []

    zoom_links = []

    raw_links1 = []

    jpg_links = []

    for x in soup.find_all("a"):
        raw_links.append(x.get("href"))



    for y in range(0, len(raw_links)):
        if raw_links[y].find(".jpg") > 0:
            zoom_links.append("bing.com" + raw_links[y])

    
    for o in zoom_links:

        req = Request(o, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

        webpage = urlopen(req).read()

        soup = bs.BeautifulSoup(webpage, "lxml")

        for x in soup.find_all("div"):
            raw_links1.append(x.get("img"))



        for y in range(0, len(raw_links1)):
            if raw_links1[y].find(".jpg") > 0:
                jpg_links.append("bing.com" + raw_links[y])

    print(jpg_links)

    input()

    ## Logic to remove duplicate links
    for c in jpg_links:
        if jpg_links.count(c) == 2:
            jpg_links.remove(c)

    n = 1
    for y in range(0, len(jpg_links)):
        dl = str(jpg_links[y])
        r = requests.get(dl, allow_redirects=True)
        open(r"Source Files\bin\image_{}.jpg".format(n), "wb").write(r.content)
        n += 1



search = input("Enter a search term\n")

scrape_bing(search)

input("Program Complete - Press enter to close")