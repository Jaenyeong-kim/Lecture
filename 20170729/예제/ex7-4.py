# -*- coding: utf-8 -*-

# ex7-4 ���� ���� ��� �����

def findCommon(A, B):
	C = []

	for a in A:
		if not a in C:
			if a in B:
				C.append(a)

	return C

tom = ['car', 'dog', 'house', 'car', 'bike', 'yacht']
bob = ['horse', 'car', 'dog', 'cat']

print "���� ���� ���:"
print findCommon(tom, bob)