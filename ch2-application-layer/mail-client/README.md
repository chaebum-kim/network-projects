## Assignment 3 : Mail Client

A simple mail client that can send email with both text and image using Google mail server.<br>

### How to run
1. Change the multipart message header from line 15 to line 17
```python
msg["To"] = 'alice@gmail.com' # email address of the recipient
msg["From"] = 'bob@gmail.com' # your email address
msg["Subject"] = 'Mail Client Test'
```

2. Change 'alice@gmail.com' and 'password' to **your gmail address and password** in line 78
```python
info = 'alice@gmail.com\x00alice@gmail.com\x00password'
```

3. Run MailClient.py
```
python MailClient.py
```

### Result
If MailClient.py is executed successfully, the recipient will get an email like this:

![screenshot](https://github.com/chaebum-kim/network-projects/blob/master/ch2-application-layer/mail-client/screenshot.JPG)
