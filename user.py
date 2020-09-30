class User(object):
	"""docstring for User
		Define el usuario de la billetera.
		Recibe 5 valores: 
		- nombre
		- apellido
		- codigo
		- email
		- psw
		"""
	def __init__(self, nombre, apellido, codigo, email, psw):
		self.nombre = nombre
		self.apellido = apellido
		self.codigo = codigo
		self.email = email
		self.psw = psw
	def indicarNombre(self, nombre):
		self.nombre = input("Ingrese su nombre: ")
	def indicarApellido(self, apellido):
		self.apellido = input("Ingrese su apellido: ")
	def indicarCodigo(self, codigo):
		self.codigo = codigo
	def indicarEmail(self, email):
		self.email = email
	def indicarPsw(self,psw):
		self.psw = psw
	def mostrarNombre(self):
		return self.nombre + " " + self.apellido
	def guardarUsuario(self):
		archuser = open("user.txt","a")
		archuser.write("\n"+self.nombre +","+ self.apellido+","+self.codigo+","+self.email+","+self.psw)
		archuser.close()


