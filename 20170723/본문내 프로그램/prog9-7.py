# -*- coding: utf-8 -*-

# prog9-7 ��Ͽ��� �ִ밪 ã��

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findMax(list, l, r):
	if l == r:
		return list[l]
	else:
		m = (l + r) / 2
		lmax = findMax(list, l, m)
		rmax = findMax(list, m + 1, r)

		if lmax > rmax:
			return lmax
		else:
			return rmax

list = raw_input("������ �Է��ϼ���: ").split()
deQuote(list)

print "�ִ밪 =", findMax(list, 0, len(list) - 1)