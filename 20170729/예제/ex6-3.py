# -*- coding: utf-8 -*-

# ex6-3 두 수의 합과 차를 계산

def sumDiff(x, y):
	return [x + y, abs(x - y)]

print "두 개의 수를 입력하세요:"
a = input()
b = input()

result = sumDiff(a, b)

print "합 =", result[0], "차 =", result[1]