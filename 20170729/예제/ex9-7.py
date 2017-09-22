# -*- coding: utf-8 -*-

# ex9-7 하노이탑

def hanoi(n, frm, aux, to):
	if n == 1:
		print frm, "→", to
	else:
		hanoi(n - 1, frm, to, aux)		# <1>
		print frm, "→", to				# <2>
		hanoi(n - 1, aux, frm, to)		# <3>

n = input("원반 개수? ")
print n, "개의 원반이면,"

hanoi(n, 'A', 'B', 'C')