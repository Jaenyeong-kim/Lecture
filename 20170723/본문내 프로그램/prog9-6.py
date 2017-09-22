# -*- coding: utf-8 -*-

# prog9-6 세균 증식

def countGerms(n):
	if n == 1 or n == 0:
		return 1
	else:
		n1 = countGerms(n - 1)
		n2 = countGerms(n - 2)
		return n1 + n2

days = input("날짜 수: ")

germs = countGerms(days)

print "생겨날 세균 수:", germs