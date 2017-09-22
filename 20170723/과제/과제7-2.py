# -*- coding: utf-8 -*-

# p7-2 구간내 홀수합 계산

def oddSum(a, b):
	if a < b:
		interval = range(a, b + 1)
	else:
		interval = range(b, a + 1)

	sum = 0							# 합산 초기화

	for i in interval:
		if i % 2 == 1:				# 홀수인 경우
			sum += i				# 합산

	return sum		

print "두 개의 자연수를 입력하세요:"
x = input()
y = input()

print x, "와", y, "사이의 홀수의 합은", oddSum(x, y), "입니다"