# -*- coding: utf-8 -*-

# prog9-2 �� ����� ��Ϳ�

def findSum(n):
	if n == 1:
		return 1
	else:
		return n + findSum(n - 1)

i = input("������ �Է��ϼ���: ")

print "1����", i, "������ ����", findSum(i), "�Դϴ�"