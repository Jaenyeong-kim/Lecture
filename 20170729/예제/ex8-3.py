# -*- coding: utf-8 -*-

# ex8-3 ������ ��Ͽ� ���� ����� �˻�

def member(item, list):
	i = 0
	mem = False
	
	while i < len(list) and not mem:
		if item == list[i]:
			mem = True
		else:
			i = i + 1

	return mem

tom = ['car', 'dog', 'house', 'car', 'bike', 'yacht']

item = raw_input("� ���� ��Ͽ� �ִ��� �ñ��ϼ���? ")

if member(item, tom):
	print "��, �ֽ��ϴ�"
else:
	print "�ƴϿ�, �����ϴ�"