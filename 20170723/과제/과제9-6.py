# -*- coding: utf-8 -*-

# p9-6 최단거리 및 경로 찾기

import sys										# sys module
from test_crossroads import *					# 가상의 교차로 정보

def crossInfo(cross):							# 교차로명으로부터 교차로 정보를 반환
	for c in crossroads:
		if c[0] == cross:
			return c[1]

def findMinDistPath(path, start, goal):			# 교차로 start에서 교차로 goal까지의 최단 거리와 경로를 반환
	if start == goal:
		return [0, path + [start]]
	else:
		minDist = sys.maxint					# 최단 거리 초기화
		minPath = []							# 최단 경로 초기화
		
		for c in crossInfo(start):				# 현재 교차로 start에서 한번에 갈 수 있는 모든 교차로에 대해 반복
			if not c[0] in path:				# 이미 지나온 교차로는 가지 않음
				distPath = findMinDistPath(path + [start], c[0], goal)

				dist = c[1] + distPath[0]		# 교차로 c를 거쳐 goal로 갈 경우의 거리

				if dist < minDist:				# 최단 거리 및 경로 갱신
					minDist = dist
					minPath = distPath[1]

		return [minDist, minPath]
				
minDistPath = findMinDistPath([], 'S', 'G')		# 교차로 S에서 교차로 G로 가는 최단 거리와 경로 구하기

print "최단 거리 =", minDistPath[0]				# 최단 거리
print "최단 경로 =", minDistPath[1]				# 최단 경로