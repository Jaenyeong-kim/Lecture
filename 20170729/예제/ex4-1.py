# -*- coding: utf-8 -*-

# ex4-1 ������Ϸκ��� ������ ���

ThisYear = 2016
Today = 330

print "�̸�, ����, ����(�� �ڸ� ��)�� �Է��ϼ���"
name = raw_input("�̸�: ")
yyyy = input("����: ")
mmdd = int(raw_input("����: "))

age = ThisYear - yyyy

if mmdd > Today:				# ���� ���� ���̸�
	age = age - 1				# ���̸� �ϳ� ����

print name, "���� �����̴�", age, "���Դϴ�"