# -*- coding: utf-8 -*-

# p6-3 1�⸸�� ���⿹��

def bank(deposit):
	interest = int(deposit * 0.1)				# ����
	sum = deposit + interest					# �����հ�

	return [deposit, interest, sum]				# ��� [����, ����, �����հ�] ��ȯ

dep = input("1�⸸�� ���⿹�ݿ� �󸶸� ��ġ�Ͻðڽ��ϱ�? ")

list = bank(dep)

print "����:", list[0]
print "����:", list[1]
print "�����հ�:", list[2]