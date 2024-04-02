friends=['Joseph','Glenn','Sally']
# Hay dos maneras de iterar la lista sabiendo la pos o no

for friend in friends:
    print('Hello',friend)

for i in range(len(friends)):
    friend = friends[i]
    print(i,'Hello',friend)
