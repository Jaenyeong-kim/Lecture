# -*- coding: utf-8 -*-

# prog5-15 ���� ��ȯ�ϴ� �Լ���

def square(a):
	return a * a

def addSquare(a, b):
	return square(a) + square(b)

print "�� ���� ���� �Է��ϼ���:"
x = input()
y = input()

print "�� ���� ������ ��:", addSquare(x, y)