# -*- coding: utf-8 -*-

# ex9-4-2 유전성 질환 ver.2

from test_family import *	# 가상의 가계

def check(p):
	if not record(p):
		return False
	elif patient(p):
		return True
	elif check(f(p)):
		return True
	else:
		return check(m(p))

p = raw_input("이름: ")

if check(p):
	print "양성!"
else:
	print "양성이란 증거 없음"