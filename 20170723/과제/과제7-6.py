# -*- coding: utf-8 -*-

# p7-6 �ִ� k-�����հ� �ִ� ���� ���

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findMaxSpan(list, k):
	size = len(list)						# ����� ����
	max = list[0]							# �ӽ� �ִ� ������

	for start in range(0, size - k + 1):	# 0 <= ���� �����ġ <= size - k
		sum = list[start]					# ���� �������� ���� ������ ù ���ҷ� �ʱ�ȭ

		for i in range(1, k):				# ���� ���� �� ���ҵ鿡 ���� �ݺ�
			sum += list[start + i]			# ���� �ջ�

		if sum > max:						# �ִ� k-������ ����
			max = sum						# ���� �ִ� k-������
			maxStart = start				# ���� �ִ� ���� ������
			maxStop = start + k - 1			# ���� �ִ� ���� ������

	return [max, maxStart, maxStop]

list = raw_input("�������� ����� �Է��ϼ���: ").split()
deQuote(list)
k = input("�ִ� k-�������� ���� ���� ��(k): ")

maxList = findMaxSpan(list, k)

print "�ִ�", k,"-������:", maxList[0]		# �ִ� k-������ �μ�
print "����:", maxList[1], ":", maxList[2]	# �ִ� ���� �μ�