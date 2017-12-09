# DrumSet
The Code / Powerpoint for a little electronic drum set

How to use:

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



BugList
	Wavplayer 
		crashes after a certian number of drum pad hits.  I think this is due because the recursion exit statment isnt working.  But hey atleast its realtimeish

	attempt2.py
		Not nearly realtime enough.  Looks like the threads might have to be made before hand and waiting for a signal to execute

	5VPad
		no debounce, and its sorely needed

	Cap_Touch_Library
		Didnt get a chance to modify the example yet, but it should be easy to do.  If your feeling brave go for it!!!