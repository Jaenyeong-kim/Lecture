# -*- coding: utf-8 -*-

# p5-5 체질량지수

def findBMI(w, h):					# BMI 계산
	return w / (h * h)

weight = input("체중? ")
height = input("신장? ") / 100.0

bmi = findBMI(weight, height)

if bmi < 20:
	print "저체중"
elif bmi < 25:
	print "정상"
elif bmi < 30:
	print "과체중"
else:
	print "비만"