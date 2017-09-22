# -*- coding: utf-8 -*-

# p8-7 세균 번식 - 다른 버전

def countDays(ngerms):			# ngerms 또는 그 이상의 세균들이 생겨나는 일짜를 계산
	a = 1						# 첫째날 생겨나는 세균 수
	b = 1						# 두째날 생겨나는 세균 수
	c = a + b					# 세째날 생겨나는 세균 수
	i = 2						# 2일째부터 계산

	while c < ngerms:			# 생겨나는 세균 수가 ngerms보다 부족한 동안 반복
		a = b					# 어제를 그제로
		b = c					# 오늘을 어제로
		c = a + b				# 그제 + 어제 = 오늘 생겨나는 세균 수
		i = i + 1				# 날짜 하루 추가갱신

	return i					# 날짜 반환

germs = input("생겨날 세균 수: ")
days = countDays(germs)

print "번식해야 할 날짜 수:", days