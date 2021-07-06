
from socket import *
from base64 import b64encode
import ssl
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# Construct multipart message
attachment = 'shibainu.jpg'

msg = MIMEMultipart()
msg["To"] = 'alice@gmail.com'
msg["From"] = 'bob@gmail.com'
msg["Subject"] = 'Mail Client Test'

msgText = MIMEText(
    f'<h3>I love computer networks!</h3><img src="cid:{attachment}">', 'html')
msg.attach(msgText)

with open(attachment, 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'inline', filename=attachment)
    img.add_header('Content-ID', f'<{attachment}>')
    msg.attach(img)

msg = msg.as_string()
endmsg = "\r\n.\r\n"

# Choose a mail server
mailserver = 'smtp.gmail.com'

# Create a socket and establish TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')
    sys.exit()

# Send HELO command and print server response
heloCommand = 'HELO alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    sys.exit()

# Start TLS connection
command = 'STARTTLS\r\n'
clientSocket.send(command.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '220':
    print('220 reply not received from server.')
    sys.exit()

# Wrap clientSocket
clientSocket = ssl.wrap_socket(clientSocket)

# Send EHLO command
heloCommand = 'EHLO alice\r\n'
clientSocket.send(heloCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
    sys.exit()


# Send AUTH command and print server response
info = 'alice@gmail.com\x00alice@gmail.com\x00password'
b64info = b64encode(info.encode()).decode('ascii')
authCommand = f'AUTH PLAIN {b64info}\r\n'
clientSocket.send(authCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '235':
    print('235 reply not received from server.')
    sys.exit()

# Send MAIL FROM command and print server response
mailFromCommand = 'MAIL FROM: <alice@gmail.com>\r\n'
clientSocket.send(mailFromCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
    sys.exit()

# Send RCPT TO command and print server response
rcptCommand = 'RCPT TO: <bob@naver.com>\r\n'
clientSocket.send(rcptCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')
    sys.exit()

# Send DATA command and print server response
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '354':
    print('354 reply not received from server')
    sys.exit()

# Send message data
for i in range(len(msg)):
    clientSocket.send(msg[i].encode())

# Message ends with a single period
clientSocket.send(endmsg.encode())

recv8 = clientSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '250':
    print('250 reply not received from server.')
    sys.exit()

# Send QUIT command and get server response
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
if recv9[:3] != '221':
    print('221 reply not received from server.')

clientSocket.close()
