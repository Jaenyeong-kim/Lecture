# -*- coding: utf-8 -*-

# ex4-3-1 ä�������� �Ǻ�			ver.1

meat = raw_input("��⸦ �����ϼ���? ")
fish = raw_input("������ �����ϼ���? ")

meatEater = meat == "yes" or fish == "yes"

if meatEater:
	print "����� ä�������ڰ� �ƴմϴ�"
else:
	print "����� ä���������Դϴ�"