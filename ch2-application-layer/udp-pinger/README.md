## Assignment 2: UDP Pinger
The goal of this assignmet is to write a client ping program in Python.<br>
The client will send 10 simple ping messages to a server and receive a<br>
corresponding pong message back from the server.<br>
The client will also output the received message and RTT of each packet<br>
if server responses. Otherwise, it will print error message.
<br>
<br>
### How to run 

1. Run UDP Pinger server
```
python UDPPingerServer.py
```
The server will be running on the **localhost**, using port number **12000**.


2. Run UDP Pinger client
```
python UDPPingerClient.py
```
![screenshot](https://github.com/chaebum-kim/network-projects/blob/master/ch2-application-layer/udp-pinger/screenshot.JPG)
