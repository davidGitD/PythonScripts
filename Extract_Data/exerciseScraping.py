import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# https://py4e-data.dr-chuck.net/comments_1997640.html web de extraccion de info

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter web: ')
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

numList = list()
# retrive all of the anchor tags
tags = soup('span')
for tag in tags:
    numList.append(int(tag.text))
    print(tag.contents[0])

print(sum(numList))