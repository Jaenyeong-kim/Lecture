# -*- coding: utf-8 -*-

# ex9-4-2 ������ ��ȯ ver.2

from test_family import *	# ������ ����

def check(p):
	if not record(p):
		return False
	elif patient(p):
		return True
	elif check(f(p)):
		return True
	else:
		return check(m(p))

p = raw_input("�̸�: ")

if check(p):
	print "�缺!"
else:
	print "�缺�̶� ���� ����"