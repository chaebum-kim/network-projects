from socket import *
import sys

try:
    if len(sys.argv) <= 1:
        print(
            'Usage: "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
        sys.exit(2)

    # Create a server socket, bind it to a port and start listening
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind((sys.argv[1], 8888))
    tcpSerSock.listen(1)

    while True:
        # Start receiving data from the client
        print('Ready to serve...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received connection from: ', addr)

        message = tcpCliSock.recv(1024).decode()
        print(message)

        # Extract the filename from the given message
        filename = message.split()[1][1:]
        fileExist = False

        try:
            # Check whether the file exists in the cache
            f = open(filename, 'r')
            outputdata = f.readlines()
            fileExist = True

            # ProxyServer finds a cache hit and generates a response message
            tcpCliSock.send('HTTP/1.0 200 OK\r\n'.encode())
            tcpCliSock.send('Content-Type:text/html\r\n'.encode())
            tcpCliSock.send('\r\n'.encode())
            for data in outputdata:
                tcpCliSock.send(data.encode())

            print('Read from cache\n')

        # Error handling for file not found in cache
        except IOError:

            if fileExist == False:
                # Create a socket on the proxy server
                c = socket(AF_INET, SOCK_STREAM)
                hostname = filename.replace('www.', '', 1)

                try:
                    # Connect to the socket to port 80
                    c.connect((hostname, 80))

                    # Ask port 80 for the file requested by the client
                    fileobj = c.makefile()
                    c.send(f'GET http://{filename} HTTP/1.0\r\n\r\n'.encode())

                    # Read the response into buffer
                    response = ''
                    while True:
                        chunk = fileobj.readline()
                        if chunk in ['\n', '\r\n']:
                            break
                        response += chunk

                    # Create a new file in the cache for the requested file
                    # Also send the response in the buffer to client socket and the corresponding file in the cache
                    with open('./' + filename, 'wb') as tmpFile:
                        data = fileobj.readlines()
                        for line in data:
                            tmpFile.write(line.encode())

                    tcpCliSock.send(response.encode())
                    tcpCliSock.send('\r\n'.encode())

                    with open('./' + filename, 'rb') as f:
                        chunk = f.read(1024)
                        while chunk:
                            tcpCliSock.send(chunk)
                            chunk = f.read(1024)

                except error as e:
                    print(e)

            else:
                # HTTP response message for file not found
                tcpCliSock.send('HTTP/1.0 404 Not Found\r\n'.encode())

        # Close the client socket
        tcpCliSock.close()

except KeyboardInterrupt:
    tcpSerSock.close()
    sys.exit()
