import bs4 as bs
import urllib.request
import shutil
from urllib.request import Request, urlopen

search = input("Enter a search term\n")

req = Request("https://www.reddit.com/r/Images/search?q={}&restrict_sr=1".format(search), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

#req = Request("https://www.reddit.com/r/Images/search?q=ocean&restrict_sr=1", headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})


webpage = urlopen(req).read()

soup = bs.BeautifulSoup(webpage, "lxml")

raw_links = []

jpg_links = []

for x in soup.find_all("a"):
    raw_links.append(x.get("href"))



for y in range(0, len(raw_links)):
    if raw_links[y].find(".jpg") > 0:
        jpg_links.append(raw_links[y])



print(raw_links)
print(jpg_links)

#print(soup)

'''response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("a")

print(response)

#imgurl = "https://www.google.com/" + aas[0]["src"]

#req.urlretrieve(imgurl, "./bin/image.png")


# ("./bin/")

'''












input("Press Enter to close")
