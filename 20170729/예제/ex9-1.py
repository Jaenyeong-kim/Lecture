# -*- coding: utf-8 -*-

# ex9-1 * 부호를 사용하지 않고 *를 계산

def product(a, b):
	if b == 1:
		return a
	else:
		return a + product(a, b - 1)

print("두 개의 자연수를 입력하세요: ")
x = input()
y = input()

print x, "*", y, "=", product(x, y)