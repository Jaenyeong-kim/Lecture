# -*- coding: utf-8 -*-

# ex7-3 목록 원소들의 평균값과 최대값

def findAverage(list):
	sum = 0

	for num in list:
		sum = sum + num

	return sum / len(list)

def findMax(list):
	largest = list[0]

	for num in list:
		if num > largest:
			largest = num

	return largest

scores = [60, 42, 50, 63, 50]

print "평균값:", findAverage(scores)
print "최대값:", findMax(scores) 