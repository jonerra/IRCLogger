# Remove tmi.twitch.tv lines from twitch logger


# Open file and read it
file = open("mango.txt", "r")
lines = file.readlines()
file.close()

# Open file and rewrite it without tmi.twitch.tv lines
f = open("mango.txt", "w")

for line in lines:
	if "tmi.twitch.tv" not in line:
		f.write(line)
		
f.close()