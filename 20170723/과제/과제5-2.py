# -*- coding: utf-8 -*-

# p5-2 ����� ���

def computeFee(age):			# ���̿� ���� ��� ���
	if age >= 18:				# ������ ���
		fee = 8000
	else:						# �̼����� ���
		fee = 4000

	return fee

age = input("���̰� ���Դϱ�? ")

fee = computeFee(age)

print "�����", fee, "���Դϴ�"