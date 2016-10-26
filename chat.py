from irc import *
import sys

# Channel and log in information
channel = "#" + sys.argv[1]
server = "irc.twitch.tv"
nickname = "adiosz"
password = 'oauth:3ovol56t8oj7n91jn4g2f2yxm63pul'
 
# Connect to server using above parameters
irc = IRC()
irc.connect(server, channel, password, nickname)

try:
    while True:
        text = irc.get_text()
        irc.write(text)
except KeyboardInterrupt:
    print('Interrupted')
	
	
	
