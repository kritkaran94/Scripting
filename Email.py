''' 

Krit Karan Singh
Indian Institute of Information Technology, Sricity

'''

#!/usr/bin/python
import smtplib,getpass
import os
import sys
os.system("./t2s.sh \"Welcome to Krit's mailing system\"")
print "Welcome to gmail mail sender by krit\n"
#os.system("./t2s.sh \"Enter your Email id\"")
gmailid=raw_input("Id : ")
gmailid=gmailid+"@gmail.com"
#os.system("./t2s.sh \"Enter your Password\"")
passwd=getpass.getpass("Gmail Password: ")
#os.system("./t2s.sh \"Enter the sunject\"")
subject=raw_input("Subject: ")
#os.system("./t2s.sh \"Enter the recepients email address\"")
line=raw_input("Recipient's email address: ")
#os.system("./t2s.sh \"Enter the body\"")
body=raw_input("Body: ")
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
sender = gmailid
recipient = line
password= passwd
body = "" + body + ""
headers = ["From: " + sender,
"Subject: " + subject,
"To: " + recipient
]
headers = "\r\n".join(headers)
session = smtplib.SMTP( 'smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()
