# -*- coding: utf-8 -*-

# p8-3 ����� ���Ұ� ��� 0 �̻��� ������ �˻�

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

#def positive(list):				# ver.1
#	n = len(list)
#	i = 0
#	pos = True
#
#	while i < n and pos:
#		if list[i] < 0:
#			pos = False
#		else:
#			i = i + 1
#
#	return pos

def positive(list):					# ver.2
	n = len(list)
	i = 0

	while i < n and list[i] >= 0:	# ��Ͽ� �˻��� ���Ұ� ���� �ְ� ���� ���Ұ� 0 �̻��� ���� ���� �ݺ�
		i = i + 1

	return i == n					# �ݺ����� ���ҵ��� ��� �˻��� �� �ϳ� �ʰ� �õ��ߴٸ� ��� �����

nums = raw_input("���� ����� �Է��ϼ���: ").split()
deQuote(nums)

if positive(nums):
	print "��� 0 �̻��� ���Դϴ�"
else:
	print "������ �����մϴ�"