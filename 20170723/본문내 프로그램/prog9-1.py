# -*- coding: utf-8 -*-

# prog9-1 잘못된 재귀예

def wrong(n):
	if n != 0:
		print "n =", n
		wrong(n - 1)
			
i = -1
wrong(i)