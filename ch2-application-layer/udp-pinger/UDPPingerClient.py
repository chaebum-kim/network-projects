
from socket import *
from datetime import datetime

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(1, 11):
    requestTime = datetime.now()
    message = f"Ping {i} {requestTime.strftime('%Y/%m/%d, %H:%M:%S')}"
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        responseTime = datetime.now()
        print(modifiedMessage.decode())
        print(f'RTT: {responseTime - requestTime}')
    except timeout:
        print("Request timed out")
