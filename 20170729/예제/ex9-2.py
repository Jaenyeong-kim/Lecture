# -*- coding: utf-8 -*-

# ex9-2 �ִ����� ���ϱ�

def gcd(a, b):
	if a == b:
		return a
	else:
		if a > b:	
			 a = a - b
		else:
			 b = b - a

		return gcd(a, b)

print "�� ���� �ڿ���: "
a = input()
b = input()

print "�ִ�����:", gcd(a, b)