# -*- coding: utf-8 -*-

# p8-2 / 부호를 사용하지 않고 /를 계산

def quotient(a, b):
	q = 0								# 몫 초기화

	while a >= b:						# 피제수가 제수보다 큰 동안 반복
		a = a - b						# 피제수에서 제수를 차감
		q = q + 1						# 몫에 1 누적

	return q							# 최종 몫을 반환

print("두 개의 자연수를 입력하세요: ")
x = input() 							# 피제수 입력
y = input() 							# 제수 입력

print x, "/", y, "=", quotient(x, y)