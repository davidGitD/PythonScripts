import json
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1997643.json'
webJson = urllib.request.urlopen(url,context=ctx).read()

dataJson = json.loads(webJson)
print('User count:', len(dataJson["comments"]))

sum = 0
for item in dataJson["comments"]:
    sum = sum+int(item["count"])

print(sum)
