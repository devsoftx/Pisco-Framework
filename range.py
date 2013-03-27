a = 10
print("inicio : " + str(0))
for i in range(a):
	print(i)

print("#################")
b = 2
c = 3
print("inicio : " + str(b))
print("interar: " + str(c))
for i in range(b,a,c):
	print(i)

print("#################")
r = range(a)
l = list(r)
print(l)
print("#################")
for i in range(10):
	if i%2 == 0:
		print("Par: " + str(i))
	else:
		print("Impar: " + str(i))