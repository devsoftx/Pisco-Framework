#first class in python
class twitter(object):	
	def __init__(self,username,password):
		self.username = username
		self.password = password

	def GetUserName(self):
		return self.username

username = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su nombre de contrasena: ")
t = twitter(username,password)
if password == "P@ssw0rd":
	print("Conectado, Usted es: ", t.GetUserName())
else:
	print("No se pudo conectarse")