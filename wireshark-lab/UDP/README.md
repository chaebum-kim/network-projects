## UDP

### Question 1
![screenshot1](https://github.com/chaebum-kim/network-projects/blob/master/wireshark-lab/UDP/screenshot1.JPG)
|No.|Question|Answer|
|---|---|---|
|1|Select one UDP packet from your trace. From this packet, determine how many fields are there in the UDP header. Name these fields.|There are 4 header fields: Source Port, Destination Port, Length, and Checksum|
<br>

### Question 2-5
![header-length](https://github.com/chaebum-kim/network-projects/blob/master/wireshark-lab/UDP/header-length.gif)

|No.|Question|Answer|
|---|---|---|
|2|By consulting the displayed information in Wireshark's packet content field for this packet, determine the length(in bytes) of each of the UDP header fields.|Each of the UDP header fields is 2-byte-long.|
|3|The value in the Length field is the length of what?|It is the length of the UDP segment(datagram).|
|4|What is the maximum number of bytes that can be included in a UDP payload?|Maximum Transmission Unit(MTU) is normally 1500 bytes. The UDP header length is 8 bytes and the ip header length is 20 bytes. So the maximum number of bytes that can be included in a UDP payload is 1500 - 8 - 20 = 1472 bytes.|
|5|What is the largest possible soure port number?|Source and Destination Port field are both 4 bytes(16 bits), so the largest possible port number is 2^16 = 65536.|
<br>

### Question 6
![screenshot2](https://github.com/chaebum-kim/network-projects/blob/master/wireshark-lab/UDP/screenshot2.JPG)
|No.|Question|Answer|
|---|---|---|
|6|What is the protocol number for UDP?|It's 17(0x11)|
<br>

### Question 7
![screenshot3](https://github.com/chaebum-kim/network-projects/blob/master/wireshark-lab/UDP/screenshot3.JPG)
|No.|Question|Answer|
|---|---|---|
|7|Examine a pair of UDP packets in which your host sends the first UDP packet and the second UDP packet is a reply to this first UDP packet. Describe the relationship between the port numbers in the two packets.|The source port number in the first UDP packet(4372) is same as the destination port number in the second UDP pacekt(4372), and the destination port number in the first UDP packet(52) is same as the source port number in the second UDP packet(52).|
