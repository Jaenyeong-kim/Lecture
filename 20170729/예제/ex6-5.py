# -*- coding: utf-8 -*-

# ex6-5 ��� ���� �μ�

def average(rec):
	name = rec[0]
	avg = (int(rec[1][0]) + int(rec[1][1]) + int(rec[1][2])) / 3
	print name, "��� =", avg 

line = raw_input("�̸��� �� ���� ����: ")
lineList = line.split()
name = lineList[0]
scoresList = lineList[1:]

average([name, scoresList])