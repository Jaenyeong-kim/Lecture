# -*- coding: utf-8 -*-

# ex8-2 * ��ȣ�� ������� �ʰ� *�� ���

def product(a, b):
	p = a

	for i in range(2, b + 1):
		p = p + a

	return p

print("�� ���� �ڿ����� �Է��ϼ���:")
x = input() 
y = input()

print x, "*", y, "=", product(x, y)