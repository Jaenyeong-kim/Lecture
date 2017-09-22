# -*- coding: utf-8 -*-

# ex7-1 범위 (1 ~ n)의 자연수들의 합

def findSum(n):
	sum = 1

	for i in range(2, n + 1):
		sum = sum + i

	return sum

i = input("자연수를 입력하세요: ")
print "1 ~", i, "사이 자연수들의 합 =", findSum(i)