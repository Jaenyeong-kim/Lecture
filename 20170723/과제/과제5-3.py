# -*- coding: utf-8 -*-

# p5-3 ��ȣ Ȯ��

def verifyTwo(two):					# �� ���ڷ� ������ ���� ��ȣ �� ���ڿ� ��ġ�ϴ��� ���� �˻�
	Password = int("0527")			# ���� ��ȣ ����

	return two == Password / 100	# �־��� �� ���ڿ� ��ȣ�� �� �� ���ڰ� ��ġ�ϴ��� ���θ� ��ȯ

passTwo = int(raw_input("��ȣ�� �� �� �ڸ��� �Է��ϼ���: "))

if verifyTwo(passTwo):
	print "��ȣ�� ��ġ�մϴ�"
else:
	print "��ȣ�� ��ġ���� �ʽ��ϴ�"