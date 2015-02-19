#!usr/bin/python

import os
import sys
import requests #module for making HTTP request
count = 0

while(1):
     response = requests.get('http://codechef.com')
     #print response #response object
     if(len(response.content)!=300):
             os.system("./t2s.sh \"BEEP BEEP BEEP BEEP CODE CODE CODE\"")
             break
     else:
        print "Count is " + count




