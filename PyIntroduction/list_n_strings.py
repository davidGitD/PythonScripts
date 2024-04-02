#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    pieces = line.split()
    print(pieces)
    
    for item in pieces:
        print('2 bucle')
        if item not in lst: # En esta linea si uso Continue, no pongo >not in<
            print('entra al if',item)
            lst.append(item)
# Al usar >>item in lst: Continue<<, cuando el item este en la lista volvera a empezar el bucle osea que no entra y sería igual a not in sin continue
lst.sort()
print(lst)