class Ave(object):
	def __init__(self,size):
		self.size = size;

class Colibri(Ave):
	def __init__(self,color):
		self.color = color;
		self.size = 50;
		self.panza = 0;

	@staticmethod
	def volar(distancia):
		for i in range(distancia):
			print("Estoy volando ", i)

	def comer(self,comida):
		if comida:
			self.panza = comida * 10;

	def GetSize(self):
		return self.size;

	def GetPanza(self):
		return self.panza;

if __name__ == "__main__":
	Colibri.volar(5)
	c = Colibri("verde")
	c.comer(3)
	print(c.GetPanza());