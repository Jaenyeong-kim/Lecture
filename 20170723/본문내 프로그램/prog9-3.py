# -*- coding: utf-8 -*-

# prog9-3 prog9-2�� �ݺ� ����

def findSum(n):
	sum = 1

	for k in range(2, n + 1):
		sum = sum + k

	return sum	

i = input("������ �Է��ϼ���: ")

print "1����", i, "������ ����", findSum(i), "�Դϴ�"