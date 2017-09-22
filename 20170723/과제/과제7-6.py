# -*- coding: utf-8 -*-

# p7-6 최대 k-구간합과 최대 구간 계산

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def findMaxSpan(list, k):
	size = len(list)						# 목록의 길이
	max = list[0]							# 임시 최대 구간합

	for start in range(0, size - k + 1):	# 0 <= 구간 출발위치 <= size - k
		sum = list[start]					# 현재 구간합을 현재 구간의 첫 원소로 초기화

		for i in range(1, k):				# 현재 구간 내 원소들에 대해 반복
			sum += list[start + i]			# 원소 합산

		if sum > max:						# 최대 k-구간합 갱신
			max = sum						# 현재 최대 k-구간합
			maxStart = start				# 현재 최대 구간 시작점
			maxStop = start + k - 1			# 현재 최대 구간 종료점

	return [max, maxStart, maxStop]

list = raw_input("정수들의 목록을 입력하세요: ").split()
deQuote(list)
k = input("최대 k-구간합을 구할 구간 수(k): ")

maxList = findMaxSpan(list, k)

print "최대", k,"-구간합:", maxList[0]		# 최대 k-구간합 인쇄
print "구간:", maxList[1], ":", maxList[2]	# 최대 구간 인쇄