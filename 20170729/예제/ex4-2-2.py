# -*- coding: utf-8 -*-

# ex4-2-2 ������/�索�� ����	ver.2

bp = input("���м�ġ: ")
bs = input("�����ġ: ")

hyper = bp > 140
hypo = bp < 90
diabete = bs > 120

if hyper or hypo or diabete:
	print "�ǽɵǴ� ��ȯ:"

	if hyper:
		print "������"
	if hypo:
		print "������"
	if diabete:
		print "�索��"