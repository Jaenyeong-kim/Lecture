# -*- coding: utf-8 -*-

# prog9-2 잘 설계된 재귀예

def findSum(n):
	if n == 1:
		return 1
	else:
		return n + findSum(n - 1)

i = input("정수를 입력하세요: ")

print "1부터", i, "까지의 합은", findSum(i), "입니다"