# -*- coding: utf-8 -*-

# ex4-2-1 ������/�索�� ����	ver.1

bp = input("���м�ġ: ")
bs = input("�����ġ: ")

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
	print "�ǽɵǴ� ��ȯ:"

	if hyper:
		print "������"
	if hypo:
		print "������"
	if diabete:
		print "�索��"