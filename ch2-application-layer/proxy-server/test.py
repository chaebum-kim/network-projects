from socket import *
import select
import threading
import sys


# Create a server socket, bind it to a port and start listening
def main():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(('127.0.0.1', 8888))
    tcpSerSock.listen(1)

    while True:
        try:
            print('Ready to serve...')
            tcpCliSock, addr = tcpSerSock.accept()
            print('Received connection from: ', addr)
            newThread = threading.Thread(
                target=clientThread, args=(tcpCliSock,))
            newThread.start()
        except KeyboardInterrupt:
            sys.exit()


def clientThread(tcpCliSock):
    tcpCliSock.setblocking(False)
    isAlive = True
    connected = False

    while True:
        # Start receiving data from the client
        message = b''
        while True:
            try:
                data = tcpCliSock.recv(1024)
                if not data:
                    isAlive = False
                message += data
            except BlockingIOError:
                break

        if not isAlive:
            tcpCliSock.close()
            return None

        if not connected and message:
            # Parse HTTP request message
            header, sep, body = message.partition(b'\r\n\r\n')
            headerlines = header.decode().split('\r\n')
            command = headerlines[0].split()[0]
            filename = headerlines[0].split()[1]
            headers = {}
            for line in headerlines[1:]:
                name, value = line.split(': ')
                headers[name] = value

            print(command, filename)
            print(headers)
            print(body)

            if command == 'CONNECT':
                proxyConn = socket(AF_INET, SOCK_STREAM)
                proxyConn.setblocking(False)
                dst = filename.split(':')
                hostname, portNum = dst[0], int(dst[1])
                try:
                    proxyConn.connect((hostname, portNum))
                except BlockingIOError:
                    select.select([], [proxyConn], [])
                    proxyConn.connect((hostname, portNum))

                tcpCliSock.send(
                    'HTTP/1.1 200 Connection Established...\r\n\r\n'.encode())
                connected = True
                print('Connection Established...')

        elif connected:
            proxyConn.send(message)
            response = b''
            while True:
                try:
                    data = proxyConn.recv(1024)
                    response += data
                except BlockingIOError:
                    break
            tcpCliSock.send(response)


if __name__ == '__main__':
    main()
