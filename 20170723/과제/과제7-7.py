# -*- coding: utf-8 -*-

# p7-7 최대 구간합 계산

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

		if sum > max:						# 최대 구간합 갱신
			max = sum
			
	return max

def findMaxAllSpans(list):
	size = len(list)						# 목록의 길이
	max = list[0]							# 임시 최대 구간합

	for k in range(1, size + 1):			# 1 <= 구간 크기 <= size
		mx = findMaxSpan(list, k)			# 최대 k-구간합, 즉 구간 크기 = k인 경우의 구간합의 최대값

		if mx > max:						# 최대 구간합 갱신
			max = mx
			
	return max

list = raw_input("정수들의 목록을 입력하세요: ").split()
deQuote(list)

max = findMaxAllSpans(list)

print "최대 구간합:", max