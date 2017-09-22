# -*- coding: utf-8 -*-

# ex7-7 세균 증식

def countGerms(n):
	if n == 0 or n == 1:
		c = 1
	else:
		a = 1
		b = 1

		for i in range(2, n + 1):
			c = a + b
			a = b
			b = c

	return c

i = input("날짜 수: ")

germs = countGerms(i)

print "생겨날 세균 수:", germs