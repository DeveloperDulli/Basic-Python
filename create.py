#!C:\Program Files\Python39\python.exe

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("content-type: text/html")
print()

import cgi, os

files = os.listdir('data')
print(files)

list_str = ''
for item in files:
    list_str = list_str + '<li> <a href="index.py?id={name}">{name}</a> </li>'.format(name=item)

form = cgi.FieldStorage()
page_id = form.getvalue('id')

if 'id' in form:
    page_id = form.getvalue('id')
    description = open('data/' + page_id,'r').read()
else:
    page_id = 'Welcome'
    description = 'Hello, Web'

print('홈페이지를 cgi로 구현')
print()
print('''
<!DOCTYPE html>
<html lang="ko" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>WEB1 - Welcome</title>
  </head>
  <body>

    <h1> <a href="index.py">WEB</a> </h1>

    <ol>
      {list_str}
    </ol>

    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description"
        placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
  </body>
</html>
'''.format(title=page_id, description=description, list_str=list_str))
