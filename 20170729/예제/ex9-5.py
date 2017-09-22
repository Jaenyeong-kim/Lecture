# -*- coding: utf-8 -*-

# ex9-5 유전성 질환 - 변형

from test_family import *	# 가상의 가계

def check(p):
	if not record(p):
		return 0
	else:
		fpos = check(f(p))
		mpos = check(m(p))

		if patient(p):
			return 1 + fpos + mpos
		else:
			return fpos + mpos
		
p = raw_input("이름: ")

if check(p) >= 3 :
	print "고위험군!"
else:
	print "고위험군 아님!"