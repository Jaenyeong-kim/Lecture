# -*- coding: utf-8 -*-

# prog7-5 ��ø for ����

kim = [520, 585]
park = [580, 540, 590]
lee = [490, 510]
students = [kim, park, lee]

def findBest(studs):
	bestAvg = -1				# bestAvg �ʱ�ȭ
	
	for s in studs:
		sum = 0					# sum �ʱ�ȭ

		for i in s:
			sum += i

		avg = sum /len(s)		# ��� ���

		if avg > bestAvg:		# �ְ� ����� ����
			bestAvg = avg
		
	return bestAvg

print "�ְ� �����: ", findBest(students)