# -*- coding: utf-8 -*-

# p9-3 % 부호를 사용하지 않고 %를 계산

def modulo(a, b):						# a % b 계산
	if a < b:							# 피제수(a)가 제수(b)보다 작은 경우
		return a						# 피제수를 나머지로 반환
	else:
		return modulo(a - b, b)			# (a - b) % b, 즉 a - b를 b로 나눈 나머지를 반환

print("두 개의 자연수를 입력하세요: ")
x = input() 							# 피제수 입력
y = input() 							# 제수 입력

print x, "%", y, "=", modulo(x, y)