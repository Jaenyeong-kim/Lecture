# -*- coding: utf-8 -*-

# ex6-3 �� ���� �հ� ���� ���

def sumDiff(x, y):
	return [x + y, abs(x - y)]

print "�� ���� ���� �Է��ϼ���:"
a = input()
b = input()

result = sumDiff(a, b)

print "�� =", result[0], "�� =", result[1]