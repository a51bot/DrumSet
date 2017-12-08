#attempt 2

#for every character that comes in open a thread for it and play a sound


import pyaudio
import wave
import sys
import threading, serial, glob

CHUNK = 1024




def play_sound(sound_f):
	wf = wave.open(sound_f, 'rb')

	# instantiate PyAudio (1)
	p = pyaudio.PyAudio()

	# open stream (2)
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True)

	# read data
	data = wf.readframes(CHUNK)

	# play stream (3)
	while len(data) > 0:
	    stream.write(data)
	    data = wf.readframes(CHUNK)

	# stop stream (4)
	stream.stop_stream()
	stream.close()

	# close PyAudio (5)
	p.terminate()



def main():
	threads = []

	#find drum files
	drums = glob.glob("./Drums/*.wav")
	if len(drums) > 0:
		print "Drums Detected"
	else:
		os.exit(1)

	#open serial port
	ser = serial.Serial('/dev/cu.usbmodemFD1341', 9600)

	prev = ""
	while True:
		x = ser.readline()
		x=x.strip()
		if x != prev:

			drum = {
				'k': drums[1],
				'1': drums[3],
				'2': drums[4],
				'3': drums[5],
				'c': drums[0],
				'r': drums[2],
				's': "",
				'h': "",


			}.get(x, "")

			#add the thread
			t = threading.Thread(target=play_sound,args=(drum,))
			threads.append(t)
			t.start()

			print x, drum
			prev = x

if __name__ == "__main__":
	main()