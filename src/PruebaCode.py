import pyfirmata
from time import sleep

def start():
	global pin8, pin9, pin10
	board=pyfirmata.Arduino('COM3')
	iter8 = pyfirmata.util.Iterator(board)
	iter8.start()
	pin8 = board.get_pin('d:8:s')
	pin9 = board.get_pin('d:9:s')
	pin10 = board.get_pin('d:10:s')
	pin8.write(0)
	sleep(1)
	pin9.write(90)
	sleep(1)
	pin10.write(90)
	sleep(1)

def MoveLeft():
	sleep(1)
	for i in range(0,90):
		pin8.write(i)

def MoveLeft():
	sleep(1)
	for i in range(0,180):
		pin8.write(i)

def MoveRight():
	sleep(1)
	for i in range(180,1,-1):
		pin8.write(i)

def Hammer(pos):
	if pos == "N":
		for i in range(90,130):
			pin9.write(i)
		for i in range(130,90,-1):
			pin9.write(i)
		sleep(1)
	elif pos == "S":
		for i in range(90,50,-1):
			pin9.write(i)
		for i in range(50,90):
			pin9.write(i)
		sleep(1)
	elif pos == "E":
		for i in range(90,130):
			pin10.write(i)
		for i in range(130,90,-1):
			pin10.write(i)
		sleep(1)
	elif pos == "O":
		for i in range(90,50,-1):
			pin10.write(i)
		for i in range(50,90):
			pin10.write(i)
		sleep(1)
	else:
		print("Error")

start()
def principal():
	MoveRight()
	MoveLeft()
	Hammer("S")
	nuevo = True
	justin = 1800
	if True:
		MoveRight()
	else:
		MoveLeft()
principal()