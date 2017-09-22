# -*- coding: utf-8 -*-

# p8-3 목록의 원소가 모두 0 이상의 수인지 검사

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

#def positive(list):				# ver.1
#	n = len(list)
#	i = 0
#	pos = True
#
#	while i < n and pos:
#		if list[i] < 0:
#			pos = False
#		else:
#			i = i + 1
#
#	return pos

def positive(list):					# ver.2
	n = len(list)
	i = 0

	while i < n and list[i] >= 0:	# 목록에 검사할 원소가 남아 있고 현재 원소가 0 이상의 수인 동안 반복
		i = i + 1

	return i == n					# 반복문이 원소들을 모두 검사한 후 하나 초과 시도했다면 모두 양수임

nums = raw_input("수의 목록을 입력하세요: ").split()
deQuote(nums)

if positive(nums):
	print "모두 0 이상의 수입니다"
else:
	print "음수가 존재합니다"