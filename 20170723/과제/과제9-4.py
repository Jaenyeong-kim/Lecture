# -*- coding: utf-8 -*-

# p9-4 ������ ��ȯ - ���� 2

from test_family import *						# ������ ����

def check(p):
	count = [0, 0]								# count ���ڸ�, �� p�� ���� �� ���� ��ȯ�� ���� 0���� �ʱ�ȭ
												# count ���ڸ�, �� p�� ���� �� ���� ��ȯ�� ���� 0���� �ʱ�ȭ
	
	if record(p):
		if record(f(p)):						# p�� �ƹ��� �Ƿ����� �ִ� ���
			fcount = check(f(p))				# p�� �ΰ� �� ���� ��ȯ�� �� fcount�� ���
			count[0] += fcount[0]				# fcount �� ���� ���� count ���ڸ��� ����
			count[1] += fcount[1]				# fcount �� ���� ���� count ���ڸ��� ����

			if patient(f(p)):					# p�� �ƹ����� ������ ��ȯ���� ���
				count[0] += 1					# count ���ڸ��� 1 �߰�
			
		if record(m(p)):						# p�� ��Ӵ� �Ƿ����� �ִ� ���
			mcount = check(m(p))				# p�� ��� �� ���� ��ȯ�� �� mcount�� ���
			count[0] += mcount[0]				# mcount �� ���� ���� count ���ڸ��� ����
			count[1] += mcount[1]				# mcount �� ���� ���� count ���ڸ��� ����

			if patient(m(p)):					# p�� ��Ӵϰ� ������ ��ȯ���� ���
				count[1] += 1					# count ���ڸ��� 1 �߰�

	return count								# count ��ȯ
		
p = raw_input("�̸�: ")							# p�� �̸� �Է�
mySex = input("����: (��=1, ��=2): ") - 1		# p�� ���� �Է�
oppositeSex = (mySex + 1) % 2					# p�� �ݴ� ����

count = check(p)								# p�� �����豺�� ���ϴ��� ���θ� �˻�

if count[mySex] > count[oppositeSex] :			# p�� ���� ������ ��ȯ�ڰ� p�� �ٸ� ������ ��ȯ�� ������ ���� ���
	print "�����豺!"
else:
	print "�����豺 �ƴ�!"