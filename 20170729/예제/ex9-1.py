# -*- coding: utf-8 -*-

# ex9-1 * ��ȣ�� ������� �ʰ� *�� ���

def product(a, b):
	if b == 1:
		return a
	else:
		return a + product(a, b - 1)

print("�� ���� �ڿ����� �Է��ϼ���: ")
x = input()
y = input()

print x, "*", y, "=", product(x, y)