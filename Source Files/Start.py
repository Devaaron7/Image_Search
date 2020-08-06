from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil


url = "https://google.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("src",)

print(soup)



#search = input("Please enter a term to image search")




# ("./bin/")














input("Press Enter to close")
