# -*- coding: utf-8 -*-

# ex8-1 ��� ������ ��ȣ�� �Էµ� ������ ���� �ݺ�

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

n = int(raw_input("����� �� �ڸ� �� ��ȣ�� �Է��ϼ���: "))

while not verify(n):
	print "����� �� ���� ��ȣ�Դϴ�"
	n = int(raw_input("����� �� �ڸ� �� ��ȣ�� �Է��ϼ���: "))

print "����� �� �ִ� ��ȣ�Դϴ�"