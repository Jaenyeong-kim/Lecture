# -*- coding: utf-8 -*-

# prog9-3 prog9-2의 반복 버전

def findSum(n):
	sum = 1

	for k in range(2, n + 1):
		sum = sum + k

	return sum	

i = input("정수를 입력하세요: ")

print "1부터", i, "까지의 합은", findSum(i), "입니다"