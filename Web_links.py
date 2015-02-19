'''

Krit Karan Singh

'''
import os
import urllib2
import re

# Getting all links from any website

# connect to the URL
website = urllib2.urlopen('http://codechef.com') # just change the name of the website as per your need
# read the Html code
html = website.read()
# use regular expressions
links = re.findall('"((http)s?://.*?)"',html)
print links
