# -*- coding: utf-8 -*-

# p7-2 ������ Ȧ���� ���

def oddSum(a, b):
	if a < b:
		interval = range(a, b + 1)
	else:
		interval = range(b, a + 1)

	sum = 0							# �ջ� �ʱ�ȭ

	for i in interval:
		if i % 2 == 1:				# Ȧ���� ���
			sum += i				# �ջ�

	return sum		

print "�� ���� �ڿ����� �Է��ϼ���:"
x = input()
y = input()

print x, "��", y, "������ Ȧ���� ����", oddSum(x, y), "�Դϴ�"