# -*- coding: utf-8 -*-

# prog9-5 �� ���ο� �� ���ھ� �μ�

def printLine(n):
	if n < 10:
		print n
	else:
		printLine(n / 10)
		print n % 10

i = input("������ �Է��ϼ���: ")

printLine(i)