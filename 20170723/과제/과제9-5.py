# -*- coding: utf-8 -*-

# p9-5 ���� ���

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findCost(lastCity, cities):									# lastCity�� ����Ͽ� ���� ���õ��� ��� �����ϴµ� ��� �ѿ��� ����Ͽ� ��ȯ
	if cities == []:											# �鷯�� �� ���ð� �� �̻� ���� ���
		return 0												# �߰��� ��� ����
	else:
		c = cities[0]											# ���� ���õ� �� ���� ���� �鷯�� �� ����
		cost = (c - lastCity) * (c - lastCity) * 10 + hotels[c]	# ���� �鷯�� �� ���ñ��� ���� ���� �� ���ÿ����� ���� ��� �ջ�
		del cities[0]											# ù��° ���� ���� �Ϸ������Ƿ� ���� ���õ� ��Ͽ��� ����

		return cost + findCost(c, cities)						# ������� ���� ���� ���õ� ���� ����� �����ؼ� ��ȯ

hotels = [0, 20, 30, 15, 30, 0]									# ���ú� ���ں�

cities = raw_input("�߰��� ������ ���õ��� �Է��ϼ���: ").split()
cities += ['5']													# �� �������� ���� �� ���ô� �׻� 5�� ����
deQuote(cities)

cost = findCost(0, cities)										# 0�� ���ø� ����Ͽ� ���� ���õ��� ��� �����ϴµ� ��� �ѿ��� ���

print "�ѿ���:", cost