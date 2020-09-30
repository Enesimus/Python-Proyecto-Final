Luego de esta introducción al mundo de las criptomonedas y las billeteras digitales, te proponemos como proyecto final del curso Fundamentos de Programación Python que desarrolles tu propia billetera digital de tipo Desktop con interfaz de texto, que soporte monedas registradas en coinmarketcap.com, y que permita:

1. Enviar un monto en USD de alguna de las criptomonedas a un destinatario indicado (identificado por un código)
2. Recibir de un enviador (identificado por un código) una cantidad de alguna criptomoneda
3. Consultar el balance de cada una de las criptomonedas en USD
4. Consultar el balance general del usuario en USD usando el precio de la criptomoneda provisto por las APIs de coinmarketcap.com
5. Emitir un histórico de transacciones del usuario indicando fecha, moneda, cantidad y monto en USD para el momento de la transacción
6. Todas las transacciones realizadas por el usuario deben ser almacenadas y mantenidas, así como las cantidades de cada una de las criptomonedas que posea

Colocar un menú de opciones con:

1. Recibir cantidad:
	- Solicitar moneda, cantidad a recibir, así como el código.
	- Validar moneda, cantidad y código, éste debe ser diferente al propio.
	- Sumar cantidad de monedas al saldo.
2. Transferir monto:
	- Solicitar moneda, monto y código del destinatario a enviar.
	- Validar.
	- Restar cantidad de monedas al saldo.
3. Mostrar balance una moneda:
	- Solicitar la moneda a mostrar
	- Validar existencia de la moneda.
	- Mostrar nombre de la moneda, cantidad y monto en USD para ese momento.
4. Mostrar balance general:
	- Mostrar nombre de cada moneda, cantidad y monto en USD para ese momento.
	- Mostrar monto total en USD de todas las monedas.
5. Mostrar histórico de transacciones:
	- Mostrar todas las transacciones indicando fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
6. Salir del programa
Recuerda hacer las validaciones de las monedas, de los montos, del saldo y de los códigos.

Consideraciones especiales:

1. Para hacer uso de las APIs de coinmarketcap.com se debe usar un API key, que se obtiene al registrase en: https://coinmarketcap.com/api/ usando el plan Basic que es gratuito.
2. Luego de registrase ingresar a https://pro.coinmarketcap.com/account, colocar el ratón  sobre la sección **API Key** (Asteriscos) y dar click en el botón **COPY KEY**.
3. En el código Python usar una variable headers, para pasar los parametros de autenticación con el API Key. Por ejemplo:
headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  'COLOCAR API KEY COPIADA'}
JavaScript
4. En la invocación del método get además del URL se deben pasar el headers y los parametros que sean necesarios. Por ejemplo:
parametros = {'symbol': symbol}
requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros)
JavaScript

En esta experiencia podrás aplicar todos los conceptos vistos en el curso y, además , podrás reutilizar la mayoría de las soluciones que has incorporado en tu portafolio a lo largo de todo este camino de aprendizaje que has recorrido en este curso ¡Éxito!

