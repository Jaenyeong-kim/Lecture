# -*- coding: utf-8 -*-

# p8-4 ��Ͽ��� Ư�� ���� �� ��� ����

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def removeAll(list, x):
	while x in list:		# ���� ��� ���Ұ� ���� �ִ� ���� �ݺ�
		list.remove(x)		# ���� ��� ���ҵ� �� ù ���Ҹ� ����

list = raw_input("����� �Է��ϼ���: ").split()
deQuote(list)

e = input("��� ���Ҹ� �����ұ��? ")

removeAll(list, e)

print "���� �� ���:", list