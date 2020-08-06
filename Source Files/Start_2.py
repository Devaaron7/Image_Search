from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil


url = "https://wallpaperaccess.com/dragon-ball-goku"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("a")

print(response)

#imgurl = "https://www.google.com/" + aas[0]["src"]

#req.urlretrieve(imgurl, "./bin/image.png")


# ("./bin/")














input("Press Enter to close")
