# -*- coding: utf-8 -*-

# prog5-13 값을 반환하는 함수예

def allotment(sum, n):
	return sum / n

price = input("상품 대금: ")
months = input("할부개월수(3~12): ")

if months < 3 or months > 12:
	print "3~12개월 할부만 가능합니다"
else:
	amt = allotment(price, months)
	print "월할부금은", amt, "입니다"