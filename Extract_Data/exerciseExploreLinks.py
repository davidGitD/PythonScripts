import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Eireyn.html'

# this function returns the 18th link in the page
def findLink(url):
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')

    # retrive all of the anchor tags
    tags = soup('a')
    counter = 0
    nextUrl = None
    for tag in tags:
        #print(counter,tag.get('href',None))
        
        if counter == 17:
            nextUrl = tag.get('href',None)
            #print('aqui esta',counter,nextUrl)
            return nextUrl
        counter = counter + 1

findLink(url)
loop = 0
while loop!=7:
    newLink = findLink(url)
    url = newLink
    loop=loop+1
    print(loop,url)

name = re.findall('by_(.+).html', url)
print('Tu nombre buscado es: ', name[0])
