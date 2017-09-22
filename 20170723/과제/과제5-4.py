# -*- coding: utf-8 -*-

# p5-4 ���� �ð� ���

def computeFlightTime(d, a):
	dhh = d / 100				# ��� �ð� �ü�
	dmm = d % 100				# ��� �ð� �м�
	ahh = a / 100				# ���� �ð� �ü�
	amm = a % 100				# ���� �ð� �м�

	if d > a:					# ���� �Ѿ� ������ ���
		ahh += 24				# ���� �ð� �ü� ����

	if dmm > amm:				# "��� �м� > ���� �м�" �� ���
		amm += 60				# ���� �ð� �м� ����
		ahh -= 1				# ���� �ð� �ü� ����

	flightTime = (ahh - dhh) * 100 + (amm - dmm)
		
	return flightTime

dep = int(raw_input("��� �ð�: "))
arr = int(raw_input("���� �ð�: "))

duration = computeFlightTime(dep, arr)

hh = duration / 100				# ���� �ð� �ü�
mm = duration % 100				# ���� �ð� �м�

if hh > 0 and mm > 0:
	print "���� �ð�: ", hh, "�ð�", mm, "��" 
elif hh > 0:
	print "���� �ð�: ", hh, "�ð�" 
elif mm > 0:
	print "���� �ð�: ", mm, "��" 