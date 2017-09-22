# -*- coding: utf-8 -*-

# prog5-15 값을 반환하는 함수예

def square(a):
	return a * a

def addSquare(a, b):
	return square(a) + square(b)

print "두 개의 수를 입력하세요:"
x = input()
y = input()

print "두 수의 제곱의 합:", addSquare(x, y)