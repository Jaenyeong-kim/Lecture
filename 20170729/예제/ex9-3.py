# -*- coding: utf-8 -*-

# ex9-3 �ִ밪 ���ϱ�

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findMax(list, l, r):
	if l == r:
		return list[l]
	else:
		max = findMax(list, l + 1, r)

		if list[l] > max:
			return list[l]
		else:
			return max

list = raw_input("������ �Է��ϼ���: ").split()
deQuote(list)

print "�ִ밪 =", findMax(list, 0, len(list) - 1)