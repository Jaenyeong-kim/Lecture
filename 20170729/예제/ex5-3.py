# -*- coding: utf-8 -*-

# ex5-3 �ﰢ���� x, y�� �ְ��� �� ������ ���ϱ�

def findMax(a, b, c):
	if a > b:
		if a > c:
			max = a
		else:
			max = c
	else:
		if b > c:
			max = b
		else:
			max = c

	return max

def findMin(a, b, c):
	if a < b:
		if a < c:
			min = a
		else:
			min = c
	else:
		if b < c:
			min = b
		else:
			min = c

	return min

print "�ﰢ���� �� �������� ��ǥ�� �Է����ּ���:"
x1 = input()
y1 = input()
x2 = input()
y2 = input()
x3 = input()
y3 = input()

print "x��: �ְ��� =", findMax(x1, x2, x3), "������ =", findMin(x1, x2, x3)

print "y��: �ְ��� =", findMax(y1, y2, y3), "������ =", findMin(y1, y2, y3)