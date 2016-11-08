from irc import *
import sys


# Channel and log in information
if len(sys.argv) == 3:
    streamers = ["#" + sys.argv[1], "#" + sys.argv[2]]
else:
    streamers = "#" + sys.argv[1]
server = "irc.twitch.tv"
nickname = "redacted"
password = 'redacted'

# Connect to server using above parameters
irc = IRC()
irc.connect(server, streamers, password, nickname)

while True:
    try:
        text = irc.get_text()
        irc.write(text)
    except KeyboardInterrupt:
        print('Interrupted')
        break

file = "chatty.txt"
irc.clean(file)
