# -*- coding: utf-8 -*-

# p9-3 % ��ȣ�� ������� �ʰ� %�� ���

def modulo(a, b):						# a % b ���
	if a < b:							# ������(a)�� ����(b)���� ���� ���
		return a						# �������� �������� ��ȯ
	else:
		return modulo(a - b, b)			# (a - b) % b, �� a - b�� b�� ���� �������� ��ȯ

print("�� ���� �ڿ����� �Է��ϼ���: ")
x = input() 							# ������ �Է�
y = input() 							# ���� �Է�

print x, "%", y, "=", modulo(x, y)