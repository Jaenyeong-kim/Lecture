# -*- coding: utf-8 -*-

# p6-2 목록에 태그 달기

def putTag(list):
	list.append(len(list))			# list의 맨끝에 태그 부착
	
list = raw_input("목록을 입력하세요: ").split()
putTag(list)

print "태그된 목록은", list, "입니다."