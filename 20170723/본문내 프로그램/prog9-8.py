# -*- coding: utf-8 -*-

# prog9-8 2�� ���� ����

def player1(board):
	board = move(board)

	if winCheck(board):
		print "player1 wins!"
		return
	else:
		print "��� �����Դϴ�"
		player2(board)

def player2(board):
	board = move(board)

	if winCheck(board):
		print "player2 wins!"
		return
	else:
		print "��� �����Դϴ�"
		player1(board)

board = initialize()
player1(board)