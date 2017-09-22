# -*- coding: utf-8 -*-

# p7-4 목록의 특정값 원소 대체

def replace(list, x, y):
	for i in range(0, len(list)):
		if list[i] == x:			# 대체 대상 원소면
			list[i] = y				# 대체

list = raw_input("목록 원소들을 입력하세요: ").split()
x = raw_input("대체 대상 원소: ")
y = raw_input("대체 원소: ")

replace(list, x, y)

print "갱신된 목록:", list