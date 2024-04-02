# Lee el doc.txt y cuenta las lineas 

file = open('doc.txt')

def countLines():
    count = 0
    for line in file:
        print(line)
        count = count + 1
    print('Este texto tiene:',count,'lineas')

def skipLines():
    for line in file:
        line = line.rstrip()
        if not line.startswith('El'):
            print(line)

def openAskedFile(file):
    try:
        file = open(file)
    except:
        print('File',file,'cannot be opened')
        quit()#quit() hace que finalice el programa en esta linea y no vaya más allá, útil para estos casos
    count = 0
    for line in file:
        print(line)
        count = count + 1
    print('Este texto tiene:',count,'lineas')

    
nameFile = input('Enter the file name: ')
openAskedFile(nameFile)