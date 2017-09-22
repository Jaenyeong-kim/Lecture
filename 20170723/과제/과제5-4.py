# -*- coding: utf-8 -*-

# p5-4 운항 시간 계산

def computeFlightTime(d, a):
	dhh = d / 100				# 출발 시각 시수
	dmm = d % 100				# 출발 시각 분수
	ahh = a / 100				# 도착 시각 시수
	amm = a % 100				# 도착 시각 분수

	if d > a:					# 자정 넘어 비행인 경우
		ahh += 24				# 도착 시각 시수 조정

	if dmm > amm:				# "출발 분수 > 도착 분수" 인 경우
		amm += 60				# 도착 시각 분수 조정
		ahh -= 1				# 도착 시각 시수 조정

	flightTime = (ahh - dhh) * 100 + (amm - dmm)
		
	return flightTime

dep = int(raw_input("출발 시각: "))
arr = int(raw_input("도착 시각: "))

duration = computeFlightTime(dep, arr)

hh = duration / 100				# 운항 시간 시수
mm = duration % 100				# 운항 시간 분수

if hh > 0 and mm > 0:
	print "운항 시간: ", hh, "시간", mm, "분" 
elif hh > 0:
	print "운항 시간: ", hh, "시간" 
elif mm > 0:
	print "운항 시간: ", mm, "분" 