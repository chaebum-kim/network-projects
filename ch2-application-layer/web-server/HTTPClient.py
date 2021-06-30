
from socket import *
import sys

# Get command line arguments
if len(sys.argv) != 4:
    print('Usage: HTTPClient.py <server host> <server port> <filename>')

serverHost = sys.argv[1]
serverPort = sys.argv[2]
filename = sys.argv[3]

# Create the client socket and connect to the server socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, int(serverPort)))

# Make HTTP request message
message = f'GET /{filename} HTTP/1.1\r\n'
clientSocket.send(message.encode())

# Output received HTTP response message
response = b''
while True:
    data = clientSocket.recv(1024)
    if len(data) == 0:
        break
    response += data
print(response.decode())
