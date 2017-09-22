# -*- coding: utf-8 -*-

# ex9-2 최대공약수 구하기

def gcd(a, b):
	if a == b:
		return a
	else:
		if a > b:	
			 a = a - b
		else:
			 b = b - a

		return gcd(a, b)

print "두 개의 자연수: "
a = input()
b = input()

print "최대공약수:", gcd(a, b)