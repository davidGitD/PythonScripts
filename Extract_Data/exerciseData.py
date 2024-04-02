import re
handle= open('Extract_Data\data.txt')
numList=list()
for linea in handle:
    linea = linea.rstrip()
    x = re.findall('[0-9]+', linea)
    if len(x) > 0:
        print(x)
        numList.extend(x)

numeroEntero = list() 
for numero in numList:
    numeroEntero.append(int(numero))

print(sum(numeroEntero))
# ESTE PROGRAMA coge los numeros de todo el doc y los suma