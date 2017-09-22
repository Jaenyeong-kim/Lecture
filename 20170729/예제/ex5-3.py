# -*- coding: utf-8 -*-

# ex5-3 삼각형의 x, y축 최고점 및 최저점 구하기

def findMax(a, b, c):
	if a > b:
		if a > c:
			max = a
		else:
			max = c
	else:
		if b > c:
			max = b
		else:
			max = c

	return max

def findMin(a, b, c):
	if a < b:
		if a < c:
			min = a
		else:
			min = c
	else:
		if b < c:
			min = b
		else:
			min = c

	return min

print "삼각형의 세 꼭지점의 좌표를 입력해주세요:"
x1 = input()
y1 = input()
x2 = input()
y2 = input()
x3 = input()
y3 = input()

print "x축: 최고점 =", findMax(x1, x2, x3), "최저점 =", findMin(x1, x2, x3)

print "y축: 최고점 =", findMax(y1, y2, y3), "최저점 =", findMin(y1, y2, y3)