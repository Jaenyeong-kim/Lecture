# -*- coding: utf-8 -*-

# prog5-12 값을 반환하는 함수예

def even(n):
	return n % 2 == 0

x = input("정수를 입력하세요: ")

if even(x):
	print "짝수입니다"
else:
	print "홀수입니다"