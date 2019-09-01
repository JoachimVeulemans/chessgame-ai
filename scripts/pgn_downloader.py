from bs4 import BeautifulSoup
import re
import urllib.request
import zipfile
import os

fp = urllib.request.urlopen("https://www.pgnmentor.com/files.html")
mybytes = fp.read()

html_doc = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(html_doc, 'html.parser')

previous_link = ""

for link in soup.findAll('a', attrs={'href': re.compile("^players.*.zip")}):
    full_link = "https://www.pgnmentor.com/" + link.get('href')
    if full_link != previous_link:
        print("Downloading: " + full_link)
        previous_link = full_link
        urllib.request.urlretrieve(full_link, '../data/pgn/' + link.get('href').split("/")[1])

        with zipfile.ZipFile('../data/pgn/' + link.get('href').split("/")[1], 'r') as zip_ref:
            zip_ref.extractall('../data/pgn/')
        os.remove("../data/pgn/" + link.get('href').split("/")[1])


