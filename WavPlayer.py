import pyaudio
import wave
import time
import sys
import glob
import serial

def play_sound(sound_file):
	wf = wave.open(sound_file, 'rb')

	# instantiate PyAudio (1)
	p = pyaudio.PyAudio()

	# define callback (2)
	def callback(in_data, frame_count, time_info, status):
		data = wf.readframes(frame_count)
		return (data, pyaudio.paContinue)

	# # open stream using callback (3)
	# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	# 				channels=wf.getnchannels(),
	# 				rate=wf.getframerate(),
	# 				output=True,
	# 				stream_callback=callback)

	# start the stream (4)
	stream.start_stream()

	#wait for stream to finish (5)
	while stream.is_active():
		print "Streaming 0"
		time.sleep(0.1)

	# stop stream (6)
	stream.stop_stream()
	stream.close()
	wf.close()
	w1.close()

	# close PyAudio (7)
	p.terminate()

def main():
	#get the drum wav files
	drums = glob.glob("./Drums/*.wav")
	print drums
	if len(drums) > 0:
		print "Drums Detected"

	#open the serial port
	ser = serial.Serial('/dev/cu.usbmodemFD1341', 9600)

	prev = ""

	while True:
		x = ser.readline()
		if x != prev:
			
			if x == 'k':
				print "kick"
				play_sound(drums[1])
			if x == '1':
				play_sound(drums[3])
			if x == '2':
				play_sound(drums[4])
			if x == '3':
				play_sound(drums[5])
			if x == 'c':
				play_sound(drums[0])
			if x == 'r':
				play_sound(drums[2])
			if x == 's':
				print "TODO Snare"

			print x
			prev = x

if __name__ == "__main__":
	main()