## TCP Basics
A screenshot below represents a series of TCP segments captured while sending a large text file to a server.

![screenshot1](https://github.com/chaebum-kim/network-projects/blob/master/wireshark-lab/TCP/screenshot1.jpg)

### TCP SYN and SYNACK segment
* TCP SYN segment 
<pre><code>Transmission Control Protocol, Src Port: 1161, Dst Port: 80, Seq: 0, Len: 0
    Source Port: 1161
    Destination Port: 80
    Sequence Number: 0    (relative sequence number)
    <strong>Sequence Number (raw): 232129012</strong>
    Acknowledgment Number: 0
    Acknowledgment number (raw): 0
    0111 .... = Header Length: 28 bytes (7)
    <strong>Flags: 0x002 (SYN)</strong>
    Window: 16384
    Checksum: 0xf6e9 [unverified]
    Urgent Pointer: 0
    Options: (8 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted</code></pre>
    
    
* TCP SYNACK segment
<pre><code>Transmission Control Protocol, Src Port: 80, Dst Port: 1161, Seq: 0, Ack: 1, Len: 0
    Source Port: 80
    Destination Port: 1161
    Sequence Number: 0    (relative sequence number)
    <strong>Sequence Number (raw): 883061785</strong>
    Acknowledgment Number: 1    (relative ack number)
    Acknowledgment number (raw): 232129013
    0111 .... = Header Length: 28 bytes (7)
    <strong>Flags: 0x012 (SYN, ACK)</strong>
    Window: 5840
    Checksum: 0x774d [unverified]
    Urgent Pointer: 0
    Options: (8 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted</code></pre>

|No.|Question|Answer|
|---|---|---|
|1|What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the clinet computer and gaia.cs.umass.edu? What is ist in the segment that identifies the segment as a SYN segment?|Seq = 232129012. A SYN segment is identified by a flag(0x002) in a TCP header.|
|2|What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu to the client computer in reply to SYN? What is the value of the Acknowledgement field in the SYNACK segment? How did gaia.cs.umass.edu determine that value? What is it in the segment that identifies the segment as a SYNACK segment?|Seq = 883061785. Ack = 232129013, which is the Seq of the SYN plus 1. A SYNACK segment is identified by a flag(0x012).|


### TCP segments associated with the HTTP POST request

* TCP segments
![screenshot2](https://github.com/chaebum-kim/network-projects/blob/master/wireshark-lab/TCP/screenshot2.jpg)
* TCP segment that contains HTTP POST request
<pre><code>Transmission Control Protocol, Src Port: 1161, Dst Port: 80, Seq: 1, Ack: 1, Len: 565
    Source Port: 1161
    Destination Port: 80
    Sequence Number: 1    (relative sequence number)
    <strong>Sequence Number (raw): 232129013</strong>
    Acknowledgment Number: 1    (relative ack number)
    Acknowledgment number (raw): 883061786
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x018 (PSH, ACK)
    Window: 17520
    Checksum: 0x1fbd [unverified]
    Urgent Pointer: 0
    TCP payload (565 bytes)
Data (565 bytes)
    Data: 504f5354202f657468657265616c2d6c6162732f6c6162332d312d7265706c792e68746d…</code></pre>
    
If you decode the data in the DATA field, you will get:
<pre><code>POST /ethereal-labs/lab3-1-reply.htm HTTP/1.1 
Host: gaia.cs.umass.edu 
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.2) Gecko/20030208 Netscape/7.02 
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,video/x-mng,image/png,image/jpeg,image/gif;q=0.2,text/css,*/*;q=0.1 
Accept-Language: en-us, en;q=0.50 
Accept-Encoding: gzip, deflate, compress;q=0.9 
Accept-Charset: ISO-8859-1, utf-8;q=0.66, *;q=0.66 
Keep-Alive: 300 
Connection: keep-alive 
Referer: http://gaia.cs.umass.edu/ethereal-labs/lab3-1.htm </code></pre>

* The recevier ACKed 2 segments
![screenshot3](https://github.com/chaebum-kim/network-projects/blob/master/wireshark-lab/TCP/screenshot3.JPG)

|No.|Question|Answer|
|---|---|---|
|1|What is the sequence number of the TCP segment containing the HTTP POST command?|Seq = 232129013|
|2|Consider the TCP segment containing the HTTP POST as the first segment in the TCP connection. What are the sequence numbers of the first six segments in the TCP connection?|Seq = 232129013 (Relative Seq = 1)<br>Seq = 232129578 (Relatvie Seq = 566)<br>Seq = 232131038 (Relative Seq = 2026)<br>Seq = 232132498 (Relative Seq = 3468)<br>Seq = 232133958 (Relatvie Seq = 4946)<br>Seq = 232135418 (Relative Seq = 6406)|
|3|At what time was each segment sent? When was the ACK for each segement received?|#1: 0.026477-0.053937<br> #2: 0.041737-0.077294<br>#3: 0.054026-0.124085<br>#4: 0.54690-0.169118<br>#5: 0.077405-0.217299<br>#6: 0.078157-0.267802|
|4|What is the RTT value for each of the six segments?|#1: 0.02746<br>#2: 0.035557<br>#3: 0.070059<br>#4: 0.114426<br>#5: 0.139894<br>#6: 0.189645|
|5|What is EstimatedRTT value after the receipt of each ACK? Assume that the value of the EstimatedRTT is equal to the measured RTT for the first segment.|#1: 0.02746<br>#2: 0.02847<br>#3: 0.03367<br>#4: 0.04376<br>#5: 0.05570<br>#6: 0.07244|
|6|What is the length of each of the first six TCP segments?|619, 1514, 1514, 1514, 1514, 1514|
|7|What is the minimum amount of available buffer space advertised at the received for the entire trace? Does the lack of receiver buffer space ever throttle the sender?|The minimum receiver buffer size advertised by the receiver is 5840 in the first ACK segment. The sender is never throttled.|
|8|Are there any retransmitted segments in the trace file? What did you check for (in the trace) in order to answer this question?|No there aren't. I looked for the segments that have the same sequence number.|
|9|How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment?|The receiver typically acknowledges 1460 bytes of the data but there are cases where the recevier ACKs another received segment, which is larger than 1460 bytes.|
|10|What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value.|The TCP connection lasted about 5.42 seconds. The sender's relative sequence number is 164091 at the end of the connection. Since there was no retransmission, it means that the sender transmitted 164090 bytes. Therefore, the throughput is 164090/5.42 = 30,274bps. (Ignore the data transmitted by the receiver since it is very small amount of data.)|




    
