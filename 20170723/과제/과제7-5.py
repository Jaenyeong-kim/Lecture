# -*- coding: utf-8 -*-

# p7-5 ���� ���

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findCost(cities):
	lastCity = 0													# ���� �ֱ� �湮�� ����
	cost = 0														# �ѿ��� �ʱ�ȭ

	for c in cities:
		cost += (c - lastCity) * (c - lastCity) * 10 + hotels[c]	# ���� ��뿡 ���� ���ñ����� ���� ����� ����
		lastCity = c												# ���� ���ø� ���� �ֱ� �湮�� ���÷� ����

	return cost

hotels = [0, 20, 30, 15, 30, 0]

cities = raw_input("�߰��� �鸦 ���õ��� �Է��ϼ���(1~4): ").split()
cities += ['5']
deQuote(cities)

cost = findCost(cities)

print "�ѿ���:", cost