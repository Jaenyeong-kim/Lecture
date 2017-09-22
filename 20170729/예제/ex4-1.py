# -*- coding: utf-8 -*-

# ex4-1 생년월일로부터 만나이 계산

ThisYear = 2016
Today = 330

print "이름, 생년, 생일(네 자리 수)을 입력하세요"
name = raw_input("이름: ")
yyyy = input("생년: ")
mmdd = int(raw_input("생일: "))

age = ThisYear - yyyy

if mmdd > Today:				# 아직 생일 전이면
	age = age - 1				# 나이를 하나 뺀다

print name, "님의 만나이는", age, "세입니다"