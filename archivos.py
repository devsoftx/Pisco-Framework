def printLine():
	print("###################################")

def ReadFile(fname, mode):
	with open(fname,mode) as reader:
		data = reader.read()
		reader.close()
		print(str(data))

def WriteInFile(fname,mode,text):
	with open(fname,mode) as writter:
		writter.write(text)
		writter.close()

printLine()
ReadFile('PYTHONSTARTUP','r')
input_text = input("Ingrese su comentario: ")
if len(input_text) != 0 :
	WriteInFile('PYTHONSTARTUP','a',input_text)
printLine()
ReadFile('PYTHONSTARTUP','r')