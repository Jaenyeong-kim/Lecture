# -*- coding: utf-8 -*-

# ex9-3 최대값 구하기

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

list = raw_input("수들을 입력하세요: ").split()
deQuote(list)

print "최대값 =", findMax(list, 0, len(list) - 1)