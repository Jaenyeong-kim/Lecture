# -*- coding: utf-8 -*-

# ex4-3-1 채식주의자 판별			ver.1

meat = raw_input("고기를 좋아하세요? ")
fish = raw_input("생선을 좋아하세요? ")

meatEater = meat == "yes" or fish == "yes"

if meatEater:
	print "당신은 채식주의자가 아닙니다"
else:
	print "당신은 채식주의자입니다"