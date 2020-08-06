from bs4 import BeautifulSoup

import requests
import urllib.request as req
import shutil


url = "https://google.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.findChildren("img",)



imgurl = "https://www.google.com/" + aas[0]["src"]

req.urlretrieve(imgurl, "./bin/image.png")


# ("./bin/")














input("Press Enter to close")
