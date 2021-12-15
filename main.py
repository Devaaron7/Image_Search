import bs4 as bs
import urllib.request
import shutil
import os
from urllib.request import Request, urlopen
import requests
import random
import webbrowser
#import wx
#import gui
from guizero import App, ListBox, MenuBar, TextBox, Text, Combo, PushButton, Box


bin_path = "./bin/"
check = os.path.isdir(bin_path)
if not check:
    os.makedirs(bin_path)
else:
    pass


app = App(width=350 , height=120, title="Image Search")

text = Text(app, text="Enter A Search Term")
input_box = TextBox(app, width=175)
text = Text(app, text="")
box = Box(app, border=1.1, width="fill", height="fill")
button = PushButton(box, width="fill", text="Start Search")
app.display()



'''

class MainFrame(gui.MyFrame1): 


   def __init__(self,parent): 
      gui.MyFrame1.__init__(self,parent)  
		
   def Search_Site(self, event):
        term = self.m_textCtrl3.GetValue()
        # Source Website
        req = Request("https://unsplash.com/s/photos/{}".format(term), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

        webpage = urlopen(req).read()

        soup = bs.BeautifulSoup(webpage, "lxml")

        # Empty lists used to manage the jpeg links extracted with beautiful soup
        raw_links = []

        jpg_links = []

        rand_links = []

        # Code to filter all the href links in the HTML file

        for x in soup.find_all("a"):
            raw_links.append(x.get("href"))

        #Code to grab just the links with the "download" text in them ( hires files)

        for y in range(0, len(raw_links)):
            if raw_links[y].find("download") > 0:
                jpg_links.append(raw_links[y])

        # Code to randomly pick 3 jpegs out of the original filtered list to download

        for x in range(0, 3):
            o = jpg_links[random.randrange(0, len(jpg_links) - 1)]
            rand_links.append(o)

        # Code to save jpegs with a "Image_#" style based on how many links are saved

        n = 1
        for y in range(0, len(rand_links)):
            dl = str(rand_links[y])
            r = requests.get(dl, allow_redirects=True)
            open("./bin/image_{}.jpg".format(n), "wb").write(r.content)
            n += 1
        
        #Opens folder where download jpegs are
        os.system("cmd /c start bin")


# Starts the GUI Window        
app = wx.App(False) 
frame1 = MainFrame(None) 
frame1.Show(True) 

app.MainLoop() 


# Code to catch errors that are produced when a search term pulls no results - out of time to implement into GUI

try:
    Search_Site(search)
except ValueError:
    print("No images found for search term")
else:   
    webbrowser.open("./bin") 

'''
