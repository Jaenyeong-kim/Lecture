# -*- coding: utf-8 -*-

# prog9-4 잘못 설계된 재귀예

def findSum(n)					# ver.2
	return n + findSum(n - 1)

def findSum(n):					# ver.3
	if n == 1:
		return 1
	else:
		return n + findSum(n + 1)