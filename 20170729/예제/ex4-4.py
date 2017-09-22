# -*- coding: utf-8 -*-

# ex4-4 국제심판

print "다섯 심판의 점수는?"
r1 = input()
r2 = input()
r3 = input()
r4 = input()
r5 = input()

max = min = r1

if r2 > max:
	max = r2
elif r2 < min:
	min = r2

if r3 > max:
	max = r3
elif r3 < min:
	min = r3

if r4 > max:
	max = r4
elif r4 < min:
	min = r4

if r5 > max:
	max = r5
elif r5 < min:
	min = r5

print "최종점수:", (r1 + r2 + r3 + r4 + r5 - max - min) / 3