# -*- coding: utf-8 -*-

# ex6-4 ��� �����κ��� �հ� ���θ� ����

def average(slist):
	return (int(slist[0]) + int(slist[1]) + int(slist[2])) / 3

scores = raw_input("�� ���� ����: ")
scoresList = scores.split()

avg = average(scoresList)

if (avg >= 60):
	print "�հ��Դϴ�"
else:
	print "���հ��Դϴ�"