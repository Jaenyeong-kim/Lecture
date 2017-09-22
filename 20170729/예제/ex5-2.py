# -*- coding: utf-8 -*-

# ex5-2 세 개의 TOEFL 점수 가운데 최고점 찾기

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

print "세 번의 TOEFL 점수를 입력하세요:"
x = input()
y = input()
z = input()

print "최고점:", findMax(x, y, z)