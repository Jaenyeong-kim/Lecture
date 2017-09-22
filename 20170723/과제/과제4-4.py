# -*- coding: utf-8 -*-

# p4-4 거스름돈 계산

price = input("물건 값? ")
received = input("받은 돈? ")

change = received - price				# 거스름돈 총액 계산

if change > 50000:						# 거스름돈이 50000원을 넘는 경우
	print 50000, "x", change / 50000
	change = change % 50000

if change >= 10000:						# 남은 거스름돈이 10000원을 넘는 경우
	print 10000, "x", change / 10000
	change = change % 10000
	
if change >= 5000:						# 남은 거스름돈이 5000원을 넘는 경우
	print 5000, "x", change / 5000
	change = change % 5000

if change >= 1000:						# 남은 거스름돈이 1000원을 넘는 경우
	print 1000, "x", change / 1000