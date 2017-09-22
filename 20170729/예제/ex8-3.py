# -*- coding: utf-8 -*-

# ex8-3 원소의 목록에 대한 멤버십 검사

def member(item, list):
	i = 0
	mem = False
	
	while i < len(list) and not mem:
		if item == list[i]:
			mem = True
		else:
			i = i + 1

	return mem

tom = ['car', 'dog', 'house', 'car', 'bike', 'yacht']

item = raw_input("어떤 값이 목록에 있는지 궁금하세요? ")

if member(item, tom):
	print "예, 있습니다"
else:
	print "아니오, 없습니다"