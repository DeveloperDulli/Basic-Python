#!C:\Program Files (x86)\Python38-32\python.exe

import sys

import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("content-type:text/html")
print()

import cgi

cgi.test()
# 웹서버가 나의 파이썬에게 주는 정보를 출력 가능
