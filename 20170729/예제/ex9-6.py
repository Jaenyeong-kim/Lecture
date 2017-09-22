# -*- coding: utf-8 -*-

# ex9-6 최단 거리 찾기
import sys										# sys module
from test_crossroads import *					# 가상의 교차로 정보

def crossInfo(cross):							# 교차로명으로부터 교차로 정보를 반환
	for c in crossroads:
		if c[0] == cross:
			return c[1]

def findMinDist(path, start, goal):				# 교차로 start에서 교차로 goal까지의 최단 거리를 반환
	if start == goal:
		return 0
	else:
		minDist = sys.maxint					# 최단 거리 초기화

		for c in crossInfo(start):				# 현재 교차로 start에서 한번에 갈 수 있는 모든 교차로에 대해 반복
			if not c[0] in path:				# 이미 지나온 교차로는 가지 않음
				dist = findMinDist(path + [start], c[0], goal)

				dist = c[1] + dist				# 교차로 c를 거쳐 goal로 갈 경우의 거리

				if dist < minDist:				# 최단 거리 갱신
					minDist = dist

		return minDist
				
minDist = findMinDist([], 'S', 'G')				# 교차로 S에서 교차로 G로 가는 최단 거리 구하기

print "최단 거리 =", minDist					# 최단 거리