# -*- coding: utf-8 -*-

# ex5-1 �� �ڸ� �� ��ȣ ����		- �Լ��� ����ϴ� ����

def verify(passwd):
	p1 = (passwd / 1000) % 10	# ù��° ���� �̾Ƴ���
	p2 = (passwd / 100) % 10	# �ι�° ���� �̾Ƴ���
	p3 = (passwd / 10) % 10		# ����° ���� �̾Ƴ���
	p4 = (passwd / 1) % 10		# �׹�° ���� �̾Ƴ���

	goodPasswd = True

	if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
		goodPasswd = False
	elif p1 + 1 == p2 and p2 + 1 == p3 and p3 + 1 == p4:
		goodPasswd = False
	elif p1 - 1 == p2 and p2 - 1 == p3 and p3 - 1 == p4:
		goodPasswd = False

	return goodPasswd

passwd = int(raw_input("����ϰ��� �ϴ� ��ȣ�� �Է��ϼ���: "))

if verify(passwd):
	print "����� �� �ִ� ��ȣ�Դϴ�"
else:
	print "����� �� ���� ��ȣ�Դϴ�"