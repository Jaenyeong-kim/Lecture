# -*- coding: utf-8 -*-

# p4-4 �Ž����� ���

price = input("���� ��? ")
received = input("���� ��? ")

change = received - price				# �Ž����� �Ѿ� ���

if change > 50000:						# �Ž������� 50000���� �Ѵ� ���
	print 50000, "x", change / 50000
	change = change % 50000

if change >= 10000:						# ���� �Ž������� 10000���� �Ѵ� ���
	print 10000, "x", change / 10000
	change = change % 10000
	
if change >= 5000:						# ���� �Ž������� 5000���� �Ѵ� ���
	print 5000, "x", change / 5000
	change = change % 5000

if change >= 1000:						# ���� �Ž������� 1000���� �Ѵ� ���
	print 1000, "x", change / 1000