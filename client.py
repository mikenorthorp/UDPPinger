# client.py
# Mike Northorp
# This program sends UDP pings to a server which then responds with the message in all caps
# It also shows when a request is timed out.
# Import time and socket
import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set up counter and while loop to send 10 pings to server
numPings = 10
temp = 0

print 'Sending 10 pings to server...\n-----------------------------\n'
# send ping 10 times to server
while temp < numPings:
	temp += 1

	# Get formatted starting time
	currentTime   = time.localtime()
	formattedTime  = time.strftime("%M:%S", currentTime)
	# Build ping message to send
	pingMessage = 'Ping %d %s' %(temp, formattedTime)
	# Get start time right before sending to calculate RTT
	start = time.time()
	# Send message to server and start the timer for the RTT
	clientSocket.sendto(pingMessage, ('localhost',12000))
	#Set a timeout (1 second) to check for
	clientSocket.settimeout(1)

	# Try to receive a message back from server
	try:
		messageReturn,serverIP = clientSocket.recvfrom(1024)
		# Print out the returned message (I am a ping) in all caps
		print messageReturn
		# Get current time minus start time for the RTT
		rtt = (time.time()-start)
		# Print out the RTT
		print 'RTT: ', rtt, '\n\n'

	# If there is a timeout print request timed out
	except timeout:
		print 'Request timed out\n\n'

#Close the socket
clientSocket.close()
