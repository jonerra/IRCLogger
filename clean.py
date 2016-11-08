# Remove tmi.twitch.tv lines from twitch logger
import time

# Open file and read it
file = open("chat2.txt", "r")
lines = file.readlines()
file.close()

# Open file to write
f = open("chat2.txt", "w")

# Format unformatted lines and rewrite to file
for line in lines:
	if "tmi.twitch.tv" in line:
		word = line.find(":", 3)
		ntext = line[word:][1:]

		# Extract username
		string = line.find("!")
		nstring = line[:string][1:]

		# Extract channel
		chan = line.find("#")
		channel = line[chan:word][1:-1]

		# Get current date and time
		ctime = time.strftime("%I:%M:%S")
		cdate = time.strftime("%m/%d/%Y")
		
		new = str(channel) + "\t" + str(nstring) + "\t" + str(cdate) + "\t" + str(ctime) + "\t" + str(ntext)
		
		# Delete initial join messages
		if "adiosz" not in line:
			f.write(new)
	else:
		f.write(line)

f.close()
