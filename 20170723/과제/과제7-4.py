# -*- coding: utf-8 -*-

# p7-4 ����� Ư���� ���� ��ü

def replace(list, x, y):
	for i in range(0, len(list)):
		if list[i] == x:			# ��ü ��� ���Ҹ�
			list[i] = y				# ��ü

list = raw_input("��� ���ҵ��� �Է��ϼ���: ").split()
x = raw_input("��ü ��� ����: ")
y = raw_input("��ü ����: ")

replace(list, x, y)

print "���ŵ� ���:", list