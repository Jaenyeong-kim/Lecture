# -*- coding: utf-8 -*-

# ex8-4 �ִ����� ���ϱ�

def gcd(a, b):
	while a != b:
		if a > b:	
			 a = a - b
		else:
			 b = b - a

	return a

print "�� ���� �ڿ���: "
a = input()
b = input()

print "�ִ�����:", gcd(a, b)