# -*- coding: utf-8 -*-

# ex9-7 �ϳ���ž

def hanoi(n, frm, aux, to):
	if n == 1:
		print frm, "��", to
	else:
		hanoi(n - 1, frm, to, aux)		# <1>
		print frm, "��", to				# <2>
		hanoi(n - 1, aux, frm, to)		# <3>

n = input("���� ����? ")
print n, "���� �����̸�,"

hanoi(n, 'A', 'B', 'C')