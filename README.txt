# DrumSet
The Code / Powerpoint for a little electronic drum set

#links for software
	-Windows
		-arduino
		https://www.arduino.cc/download_handler.php?f=/arduino-1.8.5-windows.exe

		-python
		https://www.python.org/ftp/python/2.7.14/python-2.7.14.amd64.msi
		https://superuser.com/questions/143119/how-to-add-python-to-the-windows-path
	
	-Mac
		-arduino
		https://www.arduino.cc/download_handler.php?f=/arduino-1.8.5-macosx.zip 
		
		-python (should already be installed though...)
		https://www.python.org/ftp/python/2.7.14/python-2.7.14-macosx10.6.pkg

	-Linux (should be installed)
		-arduino
		https://www.arduino.cc/download_handler.php?f=/arduino-1.8.5-linux64.tar.xz
		
		-python
		sudo apt-get install python python-pip
		sudo yum install python


#How to use:

	Open one of the 3 arduino sketch examples (5vPad, capacitive_bananas, captouch)

	Compile / Upload the sketch

	install the python libraries
	"pip -r Reqirements.txt"

	then run "python WavPlayer.py"

		if you get "python is not recogized as an internal or external program"
		follow the directions on this link
		https://superuser.com/questions/143119/how-to-add-python-to-the-windows-path

	and be sure to look at and do whatever you want to the code :)


	PS:
		attempt2.py was my second attempt at writing the python side, its a little cleaner but not as realtime as my first attempt (but it doesnt crash :D)



#BugList
	Wavplayer 
		crashes after a certian number of drum pad hits.  I think this is due because the recursion exit statment isnt working.  But hey atleast its realtimeish

	attempt2.py
		Not nearly realtime enough.  Looks like the threads might have to be made before hand and waiting for a signal to execute

	5VPad
		no debounce, and its sorely needed

	Cap_Touch_Library
		Didnt get a chance to modify the example yet, but it should be easy to do.  If your feeling brave go for it!!!