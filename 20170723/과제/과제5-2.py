# -*- coding: utf-8 -*-

# p5-2 입장료 계산

def computeFee(age):			# 나이에 따른 요금 계산
	if age >= 18:				# 성인의 경우
		fee = 8000
	else:						# 미성년의 경우
		fee = 4000

	return fee

age = input("나이가 몇입니까? ")

fee = computeFee(age)

print "요금은", fee, "원입니다"