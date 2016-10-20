from irc import *
import os
import random
# import time

# Channel and log in information 
channel = "#" + sys.argv[1]
server = "irc.twitch.tv"
nickname = "adiosz"
password = 'oauth:3ovol56t8oj7n91jn4g2f2yxm63pul'
 
# Connect to server using above parameters
irc = IRC()
irc.connect(server, channel, password, nickname)

# Open text file to append new messages
# chat_text = open("chat.txt", "a")

 
try:
	while True:
		text = irc.get_text()
		irc.write(text)	
except KeyboardInterrupt:
	print 'interrupted'

	
	
	
	
