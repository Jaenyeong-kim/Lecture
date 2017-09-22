# -*- coding: utf-8 -*-

# p9-6 �ִܰŸ� �� ��� ã��

import sys										# sys module
from test_crossroads import *					# ������ ������ ����

def crossInfo(cross):							# �����θ����κ��� ������ ������ ��ȯ
	for c in crossroads:
		if c[0] == cross:
			return c[1]

def findMinDistPath(path, start, goal):			# ������ start���� ������ goal������ �ִ� �Ÿ��� ��θ� ��ȯ
	if start == goal:
		return [0, path + [start]]
	else:
		minDist = sys.maxint					# �ִ� �Ÿ� �ʱ�ȭ
		minPath = []							# �ִ� ��� �ʱ�ȭ
		
		for c in crossInfo(start):				# ���� ������ start���� �ѹ��� �� �� �ִ� ��� �����ο� ���� �ݺ�
			if not c[0] in path:				# �̹� ������ �����δ� ���� ����
				distPath = findMinDistPath(path + [start], c[0], goal)

				dist = c[1] + distPath[0]		# ������ c�� ���� goal�� �� ����� �Ÿ�

				if dist < minDist:				# �ִ� �Ÿ� �� ��� ����
					minDist = dist
					minPath = distPath[1]

		return [minDist, minPath]
				
minDistPath = findMinDistPath([], 'S', 'G')		# ������ S���� ������ G�� ���� �ִ� �Ÿ��� ��� ���ϱ�

print "�ִ� �Ÿ� =", minDistPath[0]				# �ִ� �Ÿ�
print "�ִ� ��� =", minDistPath[1]				# �ִ� ���