import urllib.request, urllib.parse, urllib.error

handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in handler:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
print(counts)
bigCount = max(counts,key = counts.get)
print("Mas apariciones: ",bigCount,counts[bigCount])