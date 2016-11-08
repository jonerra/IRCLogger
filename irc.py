import socket
import time


class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG" + chan + " " + msg + "\n")

    def connect(self, server, channels, password, botnick):
        # defines the socket
        print("connecting to:" + server)
        self.irc.connect((server, 6667))  # connects to the server
        self.irc.send("PASS " + password + "\n")
        self.irc.send("USER " + botnick + " " + botnick + " " + botnick + " :This is a fun bot\n")  # User Auth
        self.irc.send("NICK " + botnick + "\n")
        for channel in channels:
            self.irc.send("JOIN " + channel + "\n")  # join the chan

    def get_text(self):
        text = self.irc.recv(2040)  # receive the text

        if text.find('PING') != -1:
            self.irc.send('PONG ' + text.split()[1] + '\r\n')

        return text

    def write(self, text):
        if text.find('PING') == -1:
            # Extract message
            word = text.find(":", 3)
            ntext = text[word:][1:]

            # Extract username
            string = text.find("!")
            nstring = text[:string][1:]

            # Extract channel
            chan = text.find("#")
            channel = text[chan:word][1:-1]

            # Get current date and time
            ctime = time.strftime("%I:%M:%S")
            cdate = time.strftime("%m/%d/%Y")

            print('(%s) %s %s: %s') % (channel, ctime, nstring, ntext)

            # Open text file to append new messages
            chat_text = open("chatty.txt", "a")
            chat_text.write(str(channel) + "\t" + str(nstring) + "\t" + str(cdate) + "\t" + str(ctime) + "\t" + str(ntext))
            chat_text.close()
			
	def clean(self, txt):
		# Open file and read it
		file = open(txt, "r")
		lines = file.readlines()
		file.close()

		# Open file to write
		f = open(txt, "w")

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
