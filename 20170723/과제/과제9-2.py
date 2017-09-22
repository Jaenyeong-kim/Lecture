# -*- coding: utf-8 -*-

# p9-2 / 부호를 사용하지 않고 /를 계산

def quotient(a, b):						# a / b 계산
	if a < b:							# 피제수(a)가 제수(b)보다 작은 경우
		return 0						# 몫 = 0 반환
	else:
		return 1 + quotient(a - b, b)	# a - b를 b로 나누기한 몫에 1을 더해 반환

xyList = raw_input("두 개의 자연수를 입력하세요: ").split()
x = int(xyList[0]) 							# 피제수
y = int(xyList[1]) 							# 제수

print x, "/", y, "=", quotient(x, y)