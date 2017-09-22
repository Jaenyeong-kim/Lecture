# -*- coding: utf-8 -*-

# ex3-3 순월수입 계산

i = input("연간 총수입: ")
d = input("소득공제액: ")

TaxRate = 20

ad = i - d
tax = ad * TaxRate / 100
ni = (i - tax) / 12

print "소득세", tax, "을 제외한 순월수입은", ni, "입니다"