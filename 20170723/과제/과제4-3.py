# -*- coding: utf-8 -*-

# p4-3 ���������

Balance = 10000

withdrawal = input("�󸶸� �����Ͻðڽ��ϱ�: ")

if withdrawal > Balance:				# ���� ����ݾ��� �ܰ��� ���� ���
	print "�ܾ��� �����մϴ�"
else:
	print "������ ����� ��� �ܾ���", Balance - withdrawal, "�� ���� �˴ϴ�."
	print "��� �����Ͻðڽ��ϱ�?"	