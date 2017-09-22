# -*- coding: utf-8 -*-

# prog7-5 중첩 for 문예

kim = [520, 585]
park = [580, 540, 590]
lee = [490, 510]
students = [kim, park, lee]

def findBest(studs):
	bestAvg = -1				# bestAvg 초기화
	
	for s in studs:
		sum = 0					# sum 초기화

		for i in s:
			sum += i

		avg = sum /len(s)		# 평균 계산

		if avg > bestAvg:		# 최고 평균점 갱신
			bestAvg = avg
		
	return bestAvg

print "최고 평균점: ", findBest(students)