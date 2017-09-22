# -*- coding: utf-8 -*-

# prog9-5 한 라인에 한 숫자씩 인쇄

def printLine(n):
	if n < 10:
		print n
	else:
		printLine(n / 10)
		print n % 10

i = input("정수를 입력하세요: ")

printLine(i)