# -*- coding: utf-8 -*-

# prog9-7 목록에서 최대값 찾기

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

list = raw_input("수들을 입력하세요: ").split()
deQuote(list)

print "최대값 =", findMax(list, 0, len(list) - 1)