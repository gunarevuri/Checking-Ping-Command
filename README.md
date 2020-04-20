# Checking-Ping-Command to any remote server

By cloning or downloading the code 
just run in python environment to get result 
it uses only 5 echo requests from remote server 
 you can change number of echo requests from server.
 
 Super users can send hundred or more packets per second using -f option. It prints a ‘.’ when a packet is sent, and a backspace is printed when a packet is received.
 
# ping -f localhost

PING localhost (127.0.0.1) 56(84) bytes of data.

.^C
--- localhost ping statistics ---
427412 packets transmitted, 427412 received, 0% packet loss, time 10941ms
rtt min/avg/max/mdev = 0.003/0.004/1.004/0.002 ms, ipg/ewma 0.025/0.004 ms

# ping -a for sysadmin

ping -a IP 

it will respond with beep sound for each successful packet

# If we want to print out only the statistics -q optional command is used

ping -c 5 -q www.google.com

$ ping -c 5 -q 127.0.0.1 

PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.

--- 127.0.0.1 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 3998ms
rtt min/avg/max/mdev = 0.047/0.053/0.061/0.009 ms

# we can also specify through which  path(Ip address ) packets should reach server
$ ping hop1 hop2 hop3 .. hopN destination
