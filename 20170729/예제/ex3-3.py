# -*- coding: utf-8 -*-

# ex3-3 �������� ���

i = input("���� �Ѽ���: ")
d = input("�ҵ������: ")

TaxRate = 20

ad = i - d
tax = ad * TaxRate / 100
ni = (i - tax) / 12

print "�ҵ漼", tax, "�� ������ ����������", ni, "�Դϴ�"