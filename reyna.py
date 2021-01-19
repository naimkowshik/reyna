#!/usr/bin/env/python3

import sys
from urllib.error import URLError
import dns.resolver  # Installed packages: 'dnspython'
import json
import subprocess
import time
import urllib.request
import os
from time import gmtime, strftime
from urllib.error import URLError
from urllib.parse import urlsplit
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

#############################
#    COLORING YOUR SHELL    #
#############################
R = "\033[1;31m"            #
B = "\033[1;34m"            #
Y = "\033[1;33m"            #
G = "\033[32m"              #
RS = "\033[0m"              #
W = "\033[1;37m"            #
#############################
os.system("clear")
banner = ("""                                                                                                                         
              \033[1;31m@@@@@@@   \033[1;34m@@@@@@@@  \033[1;31m@@@ @@@  @@@  @@@   @@@@@@      \033[1;34m@@@@@@   \033[1;31m@@@ @@@  \033[1;34m@@@@@@   
              \033[1;31m@@@@@@@@  \033[1;34m@@@@@@@@  \033[1;31m@@@ @@@  @@@@ @@@  @@@@@@@@     \033[1;34m@@@@@@@  \033[1;31m@@@ @@@  \033[1;34m@@@@@@@  
              \033[1;31m@@!  @@@  \033[1;34m@@!       \033[1;31m@@! !@@  @@!@!@@@  @@!  @@@         \033[1;34m@@@  \033[1;31m@@! !@@      \033[1;34m@@@  
              \033[1;31m!@!  @!@  \033[1;34m!@!       \033[1;31m!@! @!!  !@!!@!@!  !@!  @!@         \033[1;34m@!@  \033[1;31m!@! @!!      \033[1;34m@!@  
              \033[1;31m@!@!!@!   \033[1;34m@!!!:!     \033[1;31m!@!@!   @!@ !!@!  @!@!@!@!     \033[1;34m@!@!!@    \033[1;31m!@!@!  \033[1;34m @!@!!@   
              \033[1;31m!!@!@!    \033[1;34m!!!!!:      \033[1;31m@!!!   !@!  !!!  !!!@!!!!     \033[1;34m!!@!@!     \033[1;31m@!!!   \033[1;34m!!@!@!   
              \033[1;31m!!: :!!   \033[1;34m!!:         \033[1;31m!!:    !!:  !!!  !!:  !!!         \033[1;34m!!:    \033[1;31m!!:        \033[1;34m!!:  
              \033[1;31m:!:  !:!  \033[1;34m:!:         \033[1;31m:!:    :!:  !:!  :!:  !:!         \033[1;34m:!:    \033[1;31m:!:        \033[1;34m:!:  
              \033[1;31m::   :::   \033[1;34m:: ::::     \033[1;31m::     ::   ::  ::   :::     \033[1;34m:: ::::     \033[1;31m::   \033[1;34m :: ::::  
               \033[1;31m:   : :  \033[1;34m: :: ::      \033[1;31m:     ::    :    :   : :      \033[1;34m: : :      \033[1;31m:      \033[1;34m: : :   
                              \033[1;34m--------------------------------------\033[0m
                               REYNA EYE RECON TOOLKIT - BY \033[1;31mk0w581k\n""")
print(" ")
print(banner)

def yesornot():
    yes_Or_Not = input("\n" + B + "Scanning Complete. " + Y + "Press " + G + "Enter To Continue " + W + "OR " + R + "CTRL + C To Stop" + RS)
    if yes_Or_Not == '':
        os.system("clear")
        print(banner)
        mainMenu()

def mainMenu():
    print("     ")
    print("        "+W+"["+G+"+"+W+"] Options :")
    print("         "+W+"└["+R+"•"+W+"]"+G+" 1."+W+" IP Address information")
    print("         " + W + "└[" + Y + "•" + W + "]" + G + " 2." + W + " Who Is Domain Scan")
    print("         " + W + "└[" + B + "•" + W + "]" + G + " 3." + W + " Robot Txt Scan")
    print("         " + W + "└[" + G + "•" + W + "]" + G + " 4." + W + " HTTP Header Grabber")
    print("         " + W + "└[" + R + "•" + W + "]" + G + " 5." + W + " Dns Map")
    print("         " + W + "└[" + Y + "•" + W + "]" + G + " 6." + W + " DNS Recon And Enumerating SRV Records")
    print("         " + W + "└[" + B + "•" + W + "]" + G + " 7." + W + " Clickjacking Test")
    print("         " + W + "└[" + G + "•" + W + "]" + G + " 8." + W + " Website WhatWeb Scan ")
    print("         " + W + "└[" + G + "•" + W + "]" + G + " 9." + W + " Link Grabber ")
    choice = int(input("\n"+W+"        ┌["+G+"+"+W+"]Choose the options\n"+W+"        └["+R+"root"+W+"@"+W+G+"reyna"+W+"]:~# "))
    if choice == 1:
        from modules import ipscan
        print(ipscan)
        yesornot()
    elif choice == 2:
        from modules import WhoIsDomain
        print(WhoIsDomain)
        yesornot()
    elif choice == 3:
        from modules import RobotTXTSCAN
        print(RobotTXTSCAN)
        yesornot()
    elif choice == 4:
        from modules import HTTPHeaderGrabber
        print(HTTPHeaderGrabber)
        yesornot()
    elif choice == 5:
        from modules import dnsmap
        print(dnsmap)
        yesornot()
    elif choice == 6:
        from modules import dnsreconandsrv
        print(dnsreconandsrv)
        yesornot()
    elif choice == 7:
        from modules import ClickjackingTest
        print(ClickjackingTest)
        yesornot()
    elif choice == 8:
        from modules import whatweb
        print(whatweb)
        yesornot()
    elif choice == 9:
        from modules import LinkGrabber
        print(LinkGrabber)
        yesornot()


if __name__== "__main__":
    mainMenu()