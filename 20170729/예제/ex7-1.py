# -*- coding: utf-8 -*-

# ex7-1 ���� (1 ~ n)�� �ڿ������� ��

def findSum(n):
	sum = 1

	for i in range(2, n + 1):
		sum = sum + i

	return sum

i = input("�ڿ����� �Է��ϼ���: ")
print "1 ~", i, "���� �ڿ������� �� =", findSum(i)