# -*- coding: utf-8 -*-

# ex4-2-2 고혈압/당뇨병 판정	ver.2

bp = input("혈압수치: ")
bs = input("혈당수치: ")

hyper = bp > 140
hypo = bp < 90
diabete = bs > 120

if hyper or hypo or diabete:
	print "의심되는 질환:"

	if hyper:
		print "고혈압"
	if hypo:
		print "저혈압"
	if diabete:
		print "당뇨병"