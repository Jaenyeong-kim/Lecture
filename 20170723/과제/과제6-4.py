# -*- coding: utf-8 -*-

# p6-4 �ֹι�ȣ�κ��� ������� ���

def getBirthday(ssn):
	yy = ssn / 10000					# ����
	mm = (ssn / 100) % 100				# ����
	dd = ssn % 100						# ����

	return [yy, mm, dd]

n = int(raw_input("�ֹι�ȣ �� 6 �ڸ�: "))

list = getBirthday(n)

print "�������:", 1900 + list[0], list[1], list[2]