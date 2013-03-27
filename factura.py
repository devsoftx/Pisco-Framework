orders = { 'LS' : '\t -Lomo Saltado' , 'AP' : '\t -Arroz con pollo' , 'PB' : '\t -Pollo a la brasa'}
prices = { 'LS' : 19.9 , 'AP' : 18.9 , 'PB' : 20.5}
qty = 0
igv = 0
total = 0
valor = 0
names = input("Ingrese su nombre: ")
print("Lista de platillos:")
for order in orders:
	print(orders[order])
order = input("Ingrese su pedido : ")
qty = input("Ingrese la cantidad: ")
if order.upper() in orders :
	total = round(int(qty)  * float(prices[order]),2)
	igv = round((total * 0.18),2)
valor = round(total - igv,2)
print(order)
print("Nombres: " + names)
print("Pedido: " + orders[order])
print("Total: " + str(total))
print("IGV: " + str(igv))
print("Valor venta: "+ str(valor)) 