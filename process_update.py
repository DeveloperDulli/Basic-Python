#!C:\Program Files\Python39\python.exe

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import cgi, os

form = cgi.FieldStorage()
pageId = form.getvalue('pageId')
title = form.getvalue('title')
description = form.getvalue('description')

opened_file = open('data/' + pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)

#Redirection
print("Location: index.py?id="+title)
print()
