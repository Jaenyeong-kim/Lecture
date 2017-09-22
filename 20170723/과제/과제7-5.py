# -*- coding: utf-8 -*-

# p7-5 여비 계산

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findCost(cities):
	lastCity = 0													# 가장 최근 방문한 도시
	cost = 0														# 총여비 초기화

	for c in cities:
		cost += (c - lastCity) * (c - lastCity) * 10 + hotels[c]	# 과거 비용에 현재 도시까지의 여행 비용을 누적
		lastCity = c												# 현재 도시를 가장 최근 방문한 도시로 설정

	return cost

hotels = [0, 20, 30, 15, 30, 0]

cities = raw_input("중간에 들를 도시들을 입력하세요(1~4): ").split()
cities += ['5']
deQuote(cities)

cost = findCost(cities)

print "총여비:", cost