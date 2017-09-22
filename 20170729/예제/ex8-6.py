# -*- coding: utf-8 -*-

# ex8-6 ��ź ������

def findNext(n, i, k):
	i = (i + k) % n

	return i

#def playGame(players, i, k):			# for ver.
#	num = len(players)
#
#	for n2 in range(0, num - 1):
#		n = num - n2					# n�� ��������(num ~ 2) �ݺ�
#		i = findNext(n, i, k)
#		print players[i], "�� ���ӿ��� ���ܵǾ����ϴ�"
#		del players[i]
#		i = (n - 1 + i - 1) % (n - 1)	# ���ο� ������
#
#	return players[0]					# ���� ������

def playGame(players, i, k):			# while ver.
	n = len(players)

	while n > 1:
		i = findNext(n, i, k)
		print players[i], "�� ���ӿ��� ���ܵǾ����ϴ�"
		del players[i]
		n -= 1
		i = (n + i - 1) % n				# ���ο� ������
		
	return players[0]					# ���� ������

players = raw_input("�÷��̾���� ���ѷ��� ������ �Է��ϼ���: ").split()
i = input("���� ��ġ�� 0 �̻��� ���� �Է��ϼ���: ")
k = input("������ �� ������� �ұ��? ")

survivor = playGame(players, i, k)

print "���� ������:", survivor