
correct = True
while correct:
    try:
        name = input('Enter file: ')
        handle = open(name)
        correct = False
    except:
        print('File',name,'cannot be opened. Try again')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigcount,bigword)