# -*- coding: utf-8 -*-

# p4-3 현금인출기

Balance = 10000

withdrawal = input("얼마를 인출하시겠습니까: ")

if withdrawal > Balance:				# 인출 희망금액이 잔고보다 많을 경우
	print "잔액이 부족합니다"
else:
	print "인출이 진행될 경우 잔액이", Balance - withdrawal, "원 남게 됩니다."
	print "계속 진행하시겠습니까?"	