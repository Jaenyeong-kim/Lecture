# -*- coding: utf-8 -*-

# ex9-4-1 ������ ��ȯ ver.1

from test_family import *	# ������ ����

def check(p):
	if not record(p):
		return False
	elif patient(p):
		return True
	else:
		fpos = check(f(p))
		mpos = check(m(p))
		return fpos or mpos

p = raw_input("�̸�: ")

if check(p):
	print "�缺!"
else:
	print "�缺�̶� ���� ����"