# -*- coding: utf-8 -*-

# ex8-4 최대공약수 구하기

def gcd(a, b):
	while a != b:
		if a > b:	
			 a = a - b
		else:
			 b = b - a

	return a

print "두 개의 자연수: "
a = input()
b = input()

print "최대공약수:", gcd(a, b)