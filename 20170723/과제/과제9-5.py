# -*- coding: utf-8 -*-

# p9-5 여비 계산

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findCost(lastCity, cities):									# lastCity를 출발하여 남은 도시들을 모두 여행하는데 드는 총여비 계산하여 반환
	if cities == []:											# 들러야 할 도시가 더 이상 없는 경우
		return 0												# 추가할 비용 없음
	else:
		c = cities[0]											# 남은 도시들 중 가장 먼저 들러야 할 도시
		cost = (c - lastCity) * (c - lastCity) * 10 + hotels[c]	# 먼저 들러야 할 도시까지 가는 비용과 그 도시에서의 숙박 비용 합산
		del cities[0]											# 첫번째 도시 여행 완료했으므로 남은 도시들 목록에서 삭제

		return cost + findCost(c, cities)						# 현재까지 여비에 남은 도시들 여행 비용을 누적해서 반환

hotels = [0, 20, 30, 15, 30, 0]									# 도시별 숙박비

cities = raw_input("중간에 경유할 도시들을 입력하세요: ").split()
cities += ['5']													# 맨 마지막에 가야 할 도시는 항상 5번 도시
deQuote(cities)

cost = findCost(0, cities)										# 0번 도시를 출발하여 남은 도시들을 모두 여행하는데 드는 총여비 계산

print "총여비:", cost