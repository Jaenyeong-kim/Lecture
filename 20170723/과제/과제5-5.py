# -*- coding: utf-8 -*-

# p5-5 ü��������

def findBMI(w, h):					# BMI ���
	return w / (h * h)

weight = input("ü��? ")
height = input("����? ") / 100.0

bmi = findBMI(weight, height)

if bmi < 20:
	print "��ü��"
elif bmi < 25:
	print "����"
elif bmi < 30:
	print "��ü��"
else:
	print "��"