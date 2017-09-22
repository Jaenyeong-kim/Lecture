# -*- coding: utf-8 -*-

# p8-4 목록에서 특정 원소 값 모두 삭제

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def removeAll(list, x):
	while x in list:		# 삭제 대상 원소가 남아 있는 동안 반복
		list.remove(x)		# 삭제 대상 원소들 중 첫 원소를 삭제

list = raw_input("목록을 입력하세요: ").split()
deQuote(list)

e = input("어느 원소를 삭제할까요? ")

removeAll(list, e)

print "삭제 후 목록:", list