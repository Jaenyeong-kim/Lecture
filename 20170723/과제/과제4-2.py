# -*- coding: utf-8 -*-

# p4-2 교양음악 Pass/Fail 판정

mid = input("중간고사 점수: ")
final = input("기말고사 점수: ")

avg = (mid * 4 + final * 6) / 10			# 중간:기말 = 40:60 비중으로 평균 계산

if avg >= 60:
	print "교양음악의 최종학점은 Pass입니다"
else:
	print "교양음악의 최종학점은 Fail입니다"