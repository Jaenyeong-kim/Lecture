# -*- coding: utf-8 -*-

# p4-2 �������� Pass/Fail ����

mid = input("�߰���� ����: ")
final = input("�⸻��� ����: ")

avg = (mid * 4 + final * 6) / 10			# �߰�:�⸻ = 40:60 �������� ��� ���

if avg >= 60:
	print "���������� ���������� Pass�Դϴ�"
else:
	print "���������� ���������� Fail�Դϴ�"