# -*- coding: utf-8 -*-

# p9-2 / ��ȣ�� ������� �ʰ� /�� ���

def quotient(a, b):						# a / b ���
	if a < b:							# ������(a)�� ����(b)���� ���� ���
		return 0						# �� = 0 ��ȯ
	else:
		return 1 + quotient(a - b, b)	# a - b�� b�� �������� �� 1�� ���� ��ȯ

xyList = raw_input("�� ���� �ڿ����� �Է��ϼ���: ").split()
x = int(xyList[0]) 							# ������
y = int(xyList[1]) 							# ����

print x, "/", y, "=", quotient(x, y)