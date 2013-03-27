#Comentario
# twitter = "codejobs"
# if twitter == "devsoftx":ss
# 	print("Mi Cuenta en twitter es @" + twitter)
# elif twitter == "codejobs":
# 	print("La cuenta oficial del canal")
# else:
# 	print("Visita @codejobs")
# is_true = 0
# if is_true:
# 	print("Primer If")
# else:
# 	print("Se fue al else")
def suma(op1,op2):
	return op1 + op2
def resta(op1,op2):
	return op1 - op2
def producto(op1,op2):
	return op1 * op2
def division(op1,op2):
	return op1/op2

result = 0
x = input("Insert a number: ")
y = input("Insert another number: ")
con1 = int(x)
con2 = int(y)
w = input("Please, select a math operation 's' for sum, 'r' for minus, 'p' for multiplication and 'd' for division: ")
if w == "s":
	result = suma(con1,con2)
elif w == "r":
	result = resta(con1,con2)
elif w == 'p':
	result = producto(con1,con2)
else:
	result = division(con1,con2)
print(result)