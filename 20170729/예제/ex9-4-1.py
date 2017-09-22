# -*- coding: utf-8 -*-

# ex9-4-1 유전성 질환 ver.1

from test_family import *	# 가상의 가계

def check(p):
	if not record(p):
		return False
	elif patient(p):
		return True
	else:
		fpos = check(f(p))
		mpos = check(m(p))
		return fpos or mpos

p = raw_input("이름: ")

if check(p):
	print "양성!"
else:
	print "양성이란 증거 없음"