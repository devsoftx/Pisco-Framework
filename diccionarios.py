dic = {1:"ola",2: "ke",3:"ase"}
for i in dic:
    print(dic[i])

newdic = {}
n = input("Ingrese el nro de elementos: ")
c = int(n)
for i in range(c):
	newdic[i] =  input("N["+str(i)+"]: ")