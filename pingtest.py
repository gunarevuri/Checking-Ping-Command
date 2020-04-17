#!/usr/bin/env python3
import os
import platform


def isUp(hostname):

    giveFeedback = False

    if platform.system() == "Windows":
        response = os.system("ping "+hostname+" -n 1")
    else:
        response = os.system("ping -c 5 " + hostname)

    isUpBool = False
    if response == 0:
        if giveFeedback:
            print(hostname, 'is up!')
        isUpBool = True
    else:
        if giveFeedback:
            print(hostname, 'is down!')

    return isUpBool

print(isUp("www.google.com")) #Example domain
print(isUp("localhost")) #Your computer
print(isUp("www.googleabs.com")) #Unresolvable hostname: https://tools.ietf.org/html/rfc6761
print(isUp("192.168.1.1")) #Pings local router
print(isUp("192.168.1.135")) #Pings a local computer - will differ for your network
