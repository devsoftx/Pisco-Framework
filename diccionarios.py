dic = {1:"Hola",2: "como",3:"estas"}
for i in dic:
    print(dic[i])

newdic = {}
n = input("Ingrese el nro de elementos")
c = int(n)
for i in range(c):
	newdic[i] =  input("N["+str(i)+"]")