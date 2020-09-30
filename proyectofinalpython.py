import requests
import getpass
# Bienvenida
print("Bienvenido a su Digital Wallet\n")
# Conexion a API de CoinmarketCap
symbol = "BTC"

headers = { 'Accepts':'application/json','X-CMC_PRO_API_KEY':'0fa38460-7d67-49c0-aff9-360cdc027bec'}

parametros = { 'symbol': symbol}

requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros)

# Ingreso de usuario
user = input("Ingrese su nombre de usuario: ")
keypass= input("Ingrese su contraseña: ")
new_user = input("Desea crear un nuevo usuario (s/n): ")
	# Validacion de usuario


# Menu inicial
print("""Opciones de inicio
	1. Recibir depósito
	2. Transferir 
	3. Balance por moneda
	4. Balance general
	5. Historial de transacciones
	6. Salir""")
menu = input("Ingrese la opción deseada: ")

if menu =="1":
	recibirDeposito()
elif menu =="2":
	transferirMoneda()
elif menu=="3":
	balanceMoneda()
elif menu=="4":
	balanceGeneral()
elif menu=="5":
	historialTransacciones()
elif menu=="6":
	salir()
else:
	print("Opción no válida, intente otra vez")


# Recibir depósito
def recibirDeposito():
        print("Recibir depósito de criptomonedas")
        moneda = input("Ingrese el nombre de la moneda: ")
	# Validar moneda
        cantidad = input("Ingrese la cantidad de " + moneda +": ")
	# validar cantidad
        codigo = input("Ingrese el código del emisor: ")
	# valid codigo

	# sumar monedas al saldo

# Transferir moneda
def transferirMoneda():
        print("Transferir criptomonedas")
        moneda = input("Ingrese el nombre de la moneda: ")
	# Validar moneda
        cantidad = input("Ingrese la cantidad de " + moneda +": ")
	# validar cantidad
        codigo = input("Ingrese el código del receptor: ")
	# validar codigo

	#restar monedas al saldo

# Balance por moneda
def balanceMoneda():
        print("Balance por moneda: ")
        moneda = ("Ingrese el nombre de la moneda: ")
	# validar moneda

	# desplegar informacion sobre la moneda : cantidad y valor en USD al momento
	# de la consulta

# Balance general
def balanceGeneral():
        print("Balance General")
	# desplegar informacion sobre cada moneda: nombre, cantidad y valor en USD
	# desplegar monto total en USD

# Historial
def historialTransacciones():
        print("Historial de transacciones")
	# desplegar todas las transacciones indicando: fecha, moneda, tipo de
	# operacion, código del usuario, cantidad y monto para el momento.



