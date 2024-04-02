import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1997642.xml'
html = urllib.request.urlopen(url,context=ctx).read()

x = ET.fromstring(html)
lst = x.findall('comments/comment')

sum = 0
for item in lst:
    #print('Name:',item.find('name').text)
    #print('Name:',item.find('count').text)
    sum = sum+int(item.find('count').text)
print(sum)