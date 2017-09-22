# -*- coding: utf-8 -*-

# ex8-2 * 부호를 사용하지 않고 *를 계산

def product(a, b):
	p = a

	for i in range(2, b + 1):
		p = p + a

	return p

print("두 개의 자연수를 입력하세요:")
x = input() 
y = input()

print x, "*", y, "=", product(x, y)