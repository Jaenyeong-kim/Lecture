# -*- coding: utf-8 -*-

# prog5-9 인자를 전달하는 함수예

def switch(a, b):
	t = a
	a = b
	b = t
	print "switch 함수에서", "a =", a, "b =", b

print "두 개의 수를 입력하세요:"
a = input()
b = input()

print "주프로그램에서", "a =", a, "b =", b

switch(a, b)

print "주프로그램에서", "a =", a, "b =", b