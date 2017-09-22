# -*- coding: utf-8 -*-

# p3-4 1년만기 정기예금

deposit = input("1년만기 정기예금에 얼마를 예치하시겠습니까? ")

interest = deposit * 0.1		# 이자
sum = deposit + interest		# 원리합계

print "원금:", deposit
print "이자:", interest
print "원리합계:", sum