# -*- coding: utf-8 -*-

# prog5-9 ���ڸ� �����ϴ� �Լ���

def switch(a, b):
	t = a
	a = b
	b = t
	print "switch �Լ�����", "a =", a, "b =", b

print "�� ���� ���� �Է��ϼ���:"
a = input()
b = input()

print "�����α׷�����", "a =", a, "b =", b

switch(a, b)

print "�����α׷�����", "a =", a, "b =", b