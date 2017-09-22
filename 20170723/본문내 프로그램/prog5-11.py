# -*- coding: utf-8 -*-

# prog5-11 반환값 사용예

def minus(x, y):
	return x - y

a = 7
b = 5

c = minus(a, b)			# 변수에 저장

print minus(a, b)		# 인쇄에 사용

d = minus(a, b) + 10	# 산술식에 사용

if minus(a, b) > 0:		# 관계식에 사용
	print "minus(a, b)의 반환값은 양수!"