# -*- coding: utf-8 -*-

# prog5-7 인자를 전달하는 함수예

def change(p, m):
	print "물건 값 =", p
	print "받은 돈 =", m
	print "거스름돈 =", m - p

price = input("물건 값? ")
money = input("받은 돈? ")

change(price, money)