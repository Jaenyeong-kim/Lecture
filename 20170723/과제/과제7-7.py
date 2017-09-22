# -*- coding: utf-8 -*-

# p7-7 �ִ� ������ ���

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

		if sum > max:						# �ִ� ������ ����
			max = sum
			
	return max

def findMaxAllSpans(list):
	size = len(list)						# ����� ����
	max = list[0]							# �ӽ� �ִ� ������

	for k in range(1, size + 1):			# 1 <= ���� ũ�� <= size
		mx = findMaxSpan(list, k)			# �ִ� k-������, �� ���� ũ�� = k�� ����� �������� �ִ밪

		if mx > max:						# �ִ� ������ ����
			max = mx
			
	return max

list = raw_input("�������� ����� �Է��ϼ���: ").split()
deQuote(list)

max = findMaxAllSpans(list)

print "�ִ� ������:", max