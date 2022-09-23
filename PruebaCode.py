from pyfirmata import Arduino, SERVO, util
from time import sleep
port="COM3"
board = Arduino(port)
def principal():
	board.digital[8].write(180)
	sleep(3000)
	board.digital[8].write(-180)
	sleep(3000)
	board.digital[10].write(40)
 	sleep(6000)
	nuevo = 2
	print("Hola")