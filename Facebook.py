
'''  

Used Facebook's Graph API to obtain information of all my facebook friends. The script below stores their profile pics in a folder

'''

#!usr/bin/python
import requests # for making HTTPS requests to facebook serveers
import os
import time
import sys
import json
import urllib2
import webbrowser
from pprint import pprint
token = '                                  ' # Each developer at facebook gets a unique access token, just google it to obtain more informatio
api_url = 'https://graph.facebook.com/v2.1/'
params = {'access_token' : token}
call = "me/friends?fields=picture.width(9999).height(9999).type(large),gender,name" # Query parameter -> gender, name 
response = requests.get(api_url + call, params=params)
# api_url + call ---> complete query -> 'https://graph.facebook.com/v2.1/me/friends?fields=picture.width(9999).height(9999).type(large),gender,name,music'
r = (json.loads(response.content))
#pprint(r)  #java script object notation

#print r['data'] -> complete data
for x in r['data']:
       #print x['name'],x['gender']
       p_url = str(x['picture']['data']['url'])
       print p_url #url corresponding to each image
       urlopen = urllib2.build_opener()
       page = urlopen.open(p_url)
       picture = page.read()
       file_name = x['name']+"_"+x['id']+".jpg"
       print file_name+" downloaded......."
       xout = open('images/'+file_name, "wb") # file mode write and binary
       xout.write(picture)
xout.close()
