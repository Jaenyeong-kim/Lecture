# -*- coding: utf-8 -*-

# ex7-6 ���� ����

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def countVotes(votes):
	earns = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	for v in votes:
		earns[v - 1] += 1

	return earns
	
def findMaxIdx(list):
	max = 0
	maxIdx = 0
	i = 0

	for num in list:
		if num > max:
			max = num
			maxIdx = i

		i = i + 1

	return maxIdx

def printEarns(earns):
	for i in range(0, len(earns)):
		print "��ȣ:", i + 1, "��ǥ ��:", earns[i]

votes = raw_input("��ǥ ����: ").split()
deQuote(votes)

earns = countVotes(votes)
winner = findMaxIdx(earns) + 1

printEarns(earns)
print "�ִٵ�ǥ��:", winner