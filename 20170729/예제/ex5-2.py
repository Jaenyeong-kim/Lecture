# -*- coding: utf-8 -*-

# ex5-2 �� ���� TOEFL ���� ��� �ְ��� ã��

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

print "�� ���� TOEFL ������ �Է��ϼ���:"
x = input()
y = input()
z = input()

print "�ְ���:", findMax(x, y, z)