# -*- coding: utf-8 -*-

# ex8-5 �װ��� ����ý���

def reserve(p, f):
	book.append([p, f])			# ���� ���� �߰�

def flight(f):
	for item in book:
		if item[1] == f:		# �װ����� ��ġ�ϸ�
			print item[0]		# �°��� �μ�

def passenger(p):
	for item in book:
		if item[0] == p:		# �°��� ��ġ�ϸ�
			print item[1]		# �װ����� �μ�

book = []						# ������� �ʱ�ȭ
cmd = raw_input("command: ").split()

while cmd[0] != 'q':
	if cmd[0] == 'r':
		reserve(cmd[1], cmd[2])
	elif cmd[0] == 'f':
		flight(cmd[1])
	elif cmd[0] == 'p':
		passenger(cmd[1])

	cmd = raw_input("command: ").split()