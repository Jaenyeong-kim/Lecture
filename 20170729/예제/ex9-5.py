# -*- coding: utf-8 -*-

# ex9-5 ������ ��ȯ - ����

from test_family import *	# ������ ����

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
		
p = raw_input("�̸�: ")

if check(p) >= 3 :
	print "�����豺!"
else:
	print "�����豺 �ƴ�!"