import socket
import sys
import time
 
 
class IRC:

	irc = socket.socket()

	def __init__(self):  
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def send(self, chan, msg):
		self.irc.send("PRIVMSG " + chan + " " + msg + "\n")

	def connect(self, server, channel, password, botnick):
		#defines the socket
		print "connecting to:"+server
		self.irc.connect((server, 6667)) #connects to the server
		self.irc.send("PASS " + password + "\n")
		self.irc.send("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot\n") #user authentication
		self.irc.send("NICK " + botnick + "\n")               
		self.irc.send("JOIN " + channel + "\n")        #join the chan

	def get_text(self):
		text=self.irc.recv(2040)  #receive the text

		if text.find('PING') != -1:                      
			self.irc.send('PONG ' + text.split() [1] + '\r\n') 

		return text
	
	def write(self, text):
		if text.find('PING') != -1:
			# Extract message
			word = text.find(":", 3)
			ntext = text[word:][1:]
			
			# Extract username
			string = text.find("!")
			nstring = text[:string][1:]
			
			# Get current date and time
			ctime = time.strftime("%I:%M:%S")
			cdate = time.strftime("%m/%d/%Y")
			
			print '%s %s: %s' % (ctime, nstring, ntext)
			
			# Open text file to append new messages
			chat_text = open("chat.txt", "a")
			chat_text.write(str(nstring) + "," + str(cdate) + "," + str(ctime) + "," + str(ntext))
			chat_text.close()