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


def scrape_google(term):
    
    req = Request("https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwix9_eMo7HrAhVpplkKHRC0DasQ_AUoAnoECCAQBA&biw=2133&bih=1041".format(term), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    webpage = urlopen(req).read()

    soup = bs.BeautifulSoup(webpage, "lxml")

    print(soup)

    input()

    raw_links = []

    jpg_links = []

    for x in soup.find_all("a"):
        raw_links.append(x.get("href"))

    
    print(raw_links)

    input()



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



search = input("Enter a search term\n")

scrape_google(search)

input("Program Complete - Press enter to close")