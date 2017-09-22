# -*- coding: utf-8 -*-

# ex9-6 �ִ� �Ÿ� ã��
import sys										# sys module
from test_crossroads import *					# ������ ������ ����

def crossInfo(cross):							# �����θ����κ��� ������ ������ ��ȯ
	for c in crossroads:
		if c[0] == cross:
			return c[1]

def findMinDist(path, start, goal):				# ������ start���� ������ goal������ �ִ� �Ÿ��� ��ȯ
	if start == goal:
		return 0
	else:
		minDist = sys.maxint					# �ִ� �Ÿ� �ʱ�ȭ

		for c in crossInfo(start):				# ���� ������ start���� �ѹ��� �� �� �ִ� ��� �����ο� ���� �ݺ�
			if not c[0] in path:				# �̹� ������ �����δ� ���� ����
				dist = findMinDist(path + [start], c[0], goal)

				dist = c[1] + dist				# ������ c�� ���� goal�� �� ����� �Ÿ�

				if dist < minDist:				# �ִ� �Ÿ� ����
					minDist = dist

		return minDist
				
minDist = findMinDist([], 'S', 'G')				# ������ S���� ������ G�� ���� �ִ� �Ÿ� ���ϱ�

print "�ִ� �Ÿ� =", minDist					# �ִ� �Ÿ�