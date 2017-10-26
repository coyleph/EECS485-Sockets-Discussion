# TCP Sockets Discussion Demo

This is just a quick demo of successfully setting up a tcp connection 
between two endpoints and sending messages.

## Instructor (students are welcome to do this as well on their own)
Determine your local IP: 
```shellsession 
$ ifconfig 
``` 
You should see 
an ip associated with your internet adapter (not your localhost IP!).  It will be listed next to "inet".
If you are having difficulty determining which one is correct, do a quick google search for "what is my ip" and 
match the result with the corresponding IP.
Use this value and replace the following line in server.py: 
```python 
IP="yourIPhere" 
``` 
Make sure you share this IP with the students 

Run the server: 
```shellsession 
$ python3 server.py 
``` 
or to run in the background: 
```shellsession 
$ python3 server.py & 
```
## Student
Using the instructor-provided IP, replace this line in client.py: 
```python 
IP="instructorIPhere" 
``` 
Replace this line in client.py with whatever message string you would like to send: 
```python 
MESSAGE="your message" 
``` 
Run the client script to send the message: 
```shellsession 
$ python3 client.py 
```
## Result
This effectively will allow any of the students to send messages to the 
instructor via TCP.  You should be able to see these messages being 
printed on the projector via the instructor's terminal.
