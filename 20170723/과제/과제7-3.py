# -*- coding: utf-8 -*-

# p7-3 ���� Ŀ���� �� ã��

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def countBJCouples(list):
	BJCouples = []								# ���� Ŀ�õ��� ��� �ʱ�ȭ

	for e in list:
		if 21 - e in list:						# ���� Ŀ�� ��븦 ã�� ���
			if not [21 - e, e] in BJCouples:	# �̹� �߰ߵ� ���� �ƴ� ���
				BJCouples.append([e, 21 - e])	# ���� Ŀ�õ� ��Ͽ� �߰�

	return len(BJCouples)						# ���� Ŀ�õ��� ���� ��ȯ

x = raw_input("�ߺ��� ���� ������ ����� �Է��ϼ���: ").split()
deQuote(x)

print countBJCouples(x), "���� ���� Ŀ���� �ֽ��ϴ�"