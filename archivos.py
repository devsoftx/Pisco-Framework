def printLine():
	print("###################################")

printLine()
fileInDisk = open('PYTHONSTARTUP' , 'r')
w = fileInDisk.read()
print(str(w))
printLine()
print("Ejecutando un archivo .py")
exec(open('diccionarios.py' , 'r').read())
printLine()
