# -*- coding: utf-8 -*-

# ex7-7 ���� ����

def countGerms(n):
	if n == 0 or n == 1:
		c = 1
	else:
		a = 1
		b = 1

		for i in range(2, n + 1):
			c = a + b
			a = b
			b = c

	return c

i = input("��¥ ��: ")

germs = countGerms(i)

print "���ܳ� ���� ��:", germs