# -*- coding: utf-8 -*-

# p8-5 ��Ͽ��� �ߺ� ���� ����

def findUnique(list):
	i = 0							# ù ���� �˻縦 ���� �غ�
	c = 0
	while i < len(list):			# ��� ���� ��ο� ���� �ݺ�
		c += 1
		e = list[i]					# ���� �˻� ��� ����

		while list.count(e) > 1:	# ���� �˻� ��� ���Ұ� �� ���� �ʰ��Ͽ� �����ϴ� ���� �ݺ�
			c += 1
			list.remove(e)			# ���� �˻� ��� ���� �� ù ���Ҹ� ����

		i += 1						# ���� ���� �˻縦 ���� �غ�
	print "c =", c

		
x = raw_input("��� ���ҵ��� �Է��ϼ���: ").split()

findUnique(x)

print "���ŵ� ���:", x