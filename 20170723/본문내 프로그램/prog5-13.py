# -*- coding: utf-8 -*-

# prog5-13 ���� ��ȯ�ϴ� �Լ���

def allotment(sum, n):
	return sum / n

price = input("��ǰ ���: ")
months = input("�Һΰ�����(3~12): ")

if months < 3 or months > 12:
	print "3~12���� �Һθ� �����մϴ�"
else:
	amt = allotment(price, months)
	print "���Һα���", amt, "�Դϴ�"