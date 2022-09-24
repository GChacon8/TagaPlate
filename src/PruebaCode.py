from pyfirmata import Arduino, SERVO, util
from time import sleep
port="COM3"
board = Arduino(port)
def principal():
	MoveRight()
	MoveLeft()
	Hammer(S)
	nuevo = True
	justin = 1800
	while True:
		MoveLeft()
