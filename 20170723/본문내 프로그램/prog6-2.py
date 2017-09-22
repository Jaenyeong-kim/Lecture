# -*- coding: utf-8 -*-

# prog6-2 목록을 반환하는 함수예

def findMaxMin(a, b, c):
	max = min = a

	if b > a:
		max = b
	else:
		min = b

	if c > max:
		max = c

	if c < min:
		min = c

	return [max, min]

print "세 개의 수를 입력하세요:"
x = input()
y = input()
z = input()

maxmin = findMaxMin(x, y, z)

print "최대값 =", maxmin[0], "최소값 =", maxmin[1]