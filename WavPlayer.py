import pyaudio
import wave
import time
import sys
import glob
import serial

#intro
#WavPlayer is a py script to play a sound based on a character over a serial port


#sources pulled from
#https://playground.arduino.cc/Interfacing/Python

#play sound (nonblocking)
def play_sound(sound_file):
	wf = wave.open(sound_file, 'rb')

	# instantiate PyAudio (1)
	p = pyaudio.PyAudio()

	# define callback (2)
	def callback(in_data, frame_count, time_info, status):
		data = wf.readframes(frame_count)
		return (data, pyaudio.paContinue)

	# open stream using callback (3)
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True,
					stream_callback=callback)

	# start the stream (4)
	stream.start_stream()

	#wait for stream to finish (5)
	while stream.is_active():
		prev = ""
		while True:
			global ser
			x = ser.readline()
			x=x.strip()
			if x != prev:

				print x == "k\n"

				global drums

				if x in "k":
					print "kick"
					play_sound(drums[1])
				if x == '1':
					print "tom 1"
					play_sound(drums[3])
				if x == '2':
					print "tom 2"
					play_sound(drums[4])
				if x == '3':
					print "tom 3"
					play_sound(drums[5])
				if x == 'c':
					print "crash"
					play_sound(drums[0])
				if x == 'r':
					print "ride"
					play_sound(drums[2])
				if x == 's':
					print "TODO Snare"

				print x
				prev = x

	# stop stream (6)
	stream.stop_stream()
	stream.close()
	wf.close() #lets see if the works
	#wf.close()

	# close PyAudio (7)
	p.terminate()

def main():
	#get the drum wav files
	global drums
	drums = glob.glob("./Drums/*.wav")
	print drums
	if len(drums) > 0:
		print "Drums Detected"
	else:
		os.exit(1)
	#open the serial port
	global ser
	ser = serial.Serial('/dev/cu.usbmodemFD1341', 9600)

	prev = ""
	while True:
		x = ser.readline()
		x=x.strip()
		if x != prev:

			print x == "k\n"

			if x in "k":
				print "kick"
				play_sound(drums[1])
			if x == '1':
				print "tom 1"
				play_sound(drums[3])
			if x == '2':
				print "tom 2"
				play_sound(drums[4])
			if x == '3':
				print "tom 3"
				play_sound(drums[5])
			if x == 'c':
				print "crash"
				play_sound(drums[0])
			if x == 'r':
				print "ride"
				play_sound(drums[2])
			if x == 's':
				print "TODO Snare"

			print x
			prev = x

if __name__ == "__main__":
	main()