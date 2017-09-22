# -*- coding: utf-8 -*-

# p8-5 목록에서 중복 원소 제거

def findUnique(list):
	i = 0							# 첫 원소 검사를 위한 준비
	c = 0
	while i < len(list):			# 목록 원소 모두에 대해 반복
		c += 1
		e = list[i]					# 현재 검사 대상 원소

		while list.count(e) > 1:	# 현재 검사 대상 원소가 한 개를 초과하여 존재하는 동안 반복
			c += 1
			list.remove(e)			# 현재 검사 대상 원소 중 첫 원소를 삭제

		i += 1						# 다음 원소 검사를 위한 준비
	print "c =", c

		
x = raw_input("목록 원소들을 입력하세요: ").split()

findUnique(x)

print "갱신된 목록:", x