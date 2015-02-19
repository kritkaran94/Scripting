####################################################
#                                                  #
#    Author : krit karan                           #
#                                                  #
#    Description : sending email via python script #                  
#                                                  #
####################################################

# Simple Mail Transfer Protocol Server :

''' SMTP server -> It's a computer that recieves outgoing mail messages from users and routes them to their intended recepients 

# authentication - StartTLS, Port - 587
# TLS Transport Layer Security is a protocol that ensures privacy between communication applications and their users on internet
# ELO identifies the server initiating the connection

'''

#!usr/bin/python

import smtplib
import getpass
import os
import sys

os.system("./t2s.sh \"Welcome  to Krit's Mail System\"")

# problem while executing a shell script -> permissions so do chmod u+rwx filename
# source ->  ://www.arclab.com/en/amlc/list-of-smtp-and-pop3-servers-mailserver-list.html

print("Krit's Mail System")
sender = raw_input("Enter Your Gmail id:") + "@gmail.com"
passwd  = getpass.getpass("Enter Your Gmail Password: ") #your password wouldn't be echoed
subject = raw_input("Enter the subject of the Email: ")
recipient = raw_input("Enter the recepient's Email address:")
body = raw_input("Enter the text you want to send him:")
smtpserver = smtplib.SMTP("smtp.gmail.com",587) # using Gmail's SMTP server
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender,passwd)
header = 'To:' + recipient + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
print header
body = header + '\n' + body
smtpserver.sendmail(sender,recipient,body)
print('done!')
smtpserver.close()







