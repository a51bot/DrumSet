import serial

# just a test to read in the drumset keys

ser = serial.Serial('/dev/cu.usbmodemFD1341', 9600)

prev = ""

while True:
	x = ser.readline()
	if x != prev:
		print x
		prev = x
