# -*- coding: utf-8 -*-

# ex7-3 ��� ���ҵ��� ��հ��� �ִ밪

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

print "��հ�:", findAverage(scores)
print "�ִ밪:", findMax(scores) 