# -*- coding: utf-8 -*-

# ex5-4 세금 계산

def findTax(i):
	if i < 1000:
		return 0

	if i < 2400:
		tax = (i - 1000) * 0.1	
		return tax

	tax = (2400 - 1000) * 0.1

	if i < 4000:
		tax = tax + (i - 2400) * 0.12
		return tax

	tax = tax + (4000 - 2400) * 0.12

	if i < 6000:
		tax = tax + (i - 4000) * 0.15
		return tax

	tax = tax + (6000 - 4000) * 0.15
	tax = tax + (i - 6000) * 0.2

	return tax

income = input("년소득을 입력하세요: ")

print "소득세 =", findTax(income)