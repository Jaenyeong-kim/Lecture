# -*- coding: utf-8 -*-

# ex4-2-1 고혈압/당뇨병 판정	ver.1

bp = input("혈압수치: ")
bs = input("혈당수치: ")

hyper = False
hypo = False

if bp > 140:
	hyper = True
elif bp < 90:
	hypo = True
	
diabete = False

if bs > 120:
	diabete = True
	
if hyper or hypo or diabete:
	print "의심되는 질환:"

	if hyper:
		print "고혈압"
	if hypo:
		print "저혈압"
	if diabete:
		print "당뇨병"