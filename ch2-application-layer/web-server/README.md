## Assignment 1: Web Server
The goal of this assignment is to develop a simple Web server in Python<br>
that is capable of processing only one request with GET method.


### How to run HTTP server
```
python HTTPServer.py
```
HTTP server will be running on the **localhost(127.0.0.1)** using port number **6789**.
<br>
### How to send HTTP request to the server
1. Use the internet browser - Enter 127.0.0.1:6789/hello.html in the address bar.<br><br>
![screenshot](https://github.com/chaebum-kim/network-projects/blob/master/ch2-application-layer/web-server/screenshot.jpg)
<br>

2. Run HTTPClient.py
```
python HTTPClient.py 127.0.0.1 6789 hello.html
```
```
HTTP/1.1 200 OK

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello</title>
</head>
<body>
    Hello, World!
</body>
</html>

```

