# -*- coding: utf-8 -*-

# ex7-2 목록의 특정 위치 원소 대체

def replaceIdx(list, i, x):
	nlist = []

	if i < 0:
		i = len(list) + i
		
	for k in range(0, len(list)):
		if k == i:
			nlist.append(x)
		else:
			nlist.append(list[k])

	return nlist

list = raw_input("목록을 입력하세요: ").split()
i = input("색인 번호: ")
x = raw_input("대체 값: ")

nlist = replaceIdx(list, i, x)

print "대체 후 목록:", nlist