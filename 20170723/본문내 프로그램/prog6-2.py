# -*- coding: utf-8 -*-

# prog6-2 ����� ��ȯ�ϴ� �Լ���

def findMaxMin(a, b, c):
	max = min = a

	if b > a:
		max = b
	else:
		min = b

	if c > max:
		max = c

	if c < min:
		min = c

	return [max, min]

print "�� ���� ���� �Է��ϼ���:"
x = input()
y = input()
z = input()

maxmin = findMaxMin(x, y, z)

print "�ִ밪 =", maxmin[0], "�ּҰ� =", maxmin[1]