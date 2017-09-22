# -*- coding: utf-8 -*-

# p6-3 1년만기 정기예금

def bank(deposit):
	interest = int(deposit * 0.1)				# 이자
	sum = deposit + interest					# 원리합계

	return [deposit, interest, sum]				# 목록 [원금, 이자, 원리합계] 반환

dep = input("1년만기 정기예금에 얼마를 예치하시겠습니까? ")

list = bank(dep)

print "원금:", list[0]
print "이자:", list[1]
print "원리합계:", list[2]