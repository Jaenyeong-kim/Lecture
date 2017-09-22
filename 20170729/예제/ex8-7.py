# -*- coding: utf-8 -*-

# ex8-7 ��ź ������ - ����

def findNext(players, sitters, num, i, k):
	counter = 0

	while counter < k:
		i = (i + 1) % num

		if not players[i] in sitters:
			counter += 1

	return i

def findLast(players, sitters, num, i):
	while players[i] in sitters:
		i = (i + 1) % num

	return i

#def playGame(players, i, k):				# for ver.
#	n = num = len(players)
#
#	for round in range(1, num):
#		i = findNext(players, sitters, num, i, k)
#		print players[i], "�� ���ӿ��� ���ܵǾ����ϴ�"
#		sitters.append(players[i])
#		
#	survivorIdx = findLast(players, sitters, num, i)
#
#	return players[survivorIdx]				# ���� ������

def playGame(players, i, k):				# while ver.
	n = num = len(players)
	sitters = []							# ���� �÷��̾��

	while n > 1:
		i = findNext(players, sitters, num, i, k)
		print players[i], "�� ���ӿ��� ���ܵǾ����ϴ�"
		sitters.append(players[i])
		n -= 1

	survivorIdx = findLast(players, sitters, num, i)
	
	return players[survivorIdx]				# ���� ������

players = raw_input("�÷��̾���� ���ѷ��� ������ �Է��ϼ���: ").split()
i = input("���� ��ġ�� 0 �̻��� ���ڷ� �Է��ϼ���: ")
k = input("������ �� ������� �ұ��? ")

survivor = playGame(players, i, k)

print "���� ������:", survivor