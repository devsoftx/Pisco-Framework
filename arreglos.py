def printList(l):
	for i in range(len(l)):
		print(str(l[i]))

def sumList(l):
	i = 0
	for x in range(len(l)):
		i = i + int(l[x])
	return i

def appendToList(l,c):
	for i in range(c):
		value = input("Elemento n[" + str(i) + "]: ")
		l.append(value)
	return l

n = input("Ingrese el numero de elementos: ")
c = int(n)
array = []
appendToList(array,c)
print("Elementos:")
printList(array)
d = sumList(array)
print("Suma: " + str(d))
x = input("N° de elementos a cortar: ")
y = int(x)
if(y > 0):
	array = appendToList(array[:y],y)	

printList(array)
sumList(array)
d = sumList(array)
print("Suma: " + str(d))