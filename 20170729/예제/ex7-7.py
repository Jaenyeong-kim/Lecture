# -*- coding: utf-8 -*-

# ex7-7 �ִ� k-������ ���
import sys									# sys ��� ����
def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findMaxSpan(list, k):
	size = len(list)						# ����� ����
	max = -sys.maxint						# �ӽ� �ִ� ������

	for start in range(0, size - k + 1):	# start = ���� ��� ��ġ
		sum = list[start]					# ���� ������ �ʱ�ȭ

		for i in range(1, k):				# ���� ���� �� ���ҵ�
			sum += list[start + i]			# ���� �ջ�

		if sum > max:						# �ִ� ������ ����
			max = sum
			
	return max

list = raw_input("�������� ����� �Է��ϼ���: ").split()
deQuote(list)
k = input("�ִ� �������� ���� ���� ��: ")

max = findMaxSpan(list, k)

print "�ִ�", k,"-������:", max