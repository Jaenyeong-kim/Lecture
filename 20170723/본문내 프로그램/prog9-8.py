# -*- coding: utf-8 -*-

# prog9-8 2인 보드 게임

def player1(board):
	board = move(board)

	if winCheck(board):
		print "player1 wins!"
		return
	else:
		print "당신 차례입니다"
		player2(board)

def player2(board):
	board = move(board)

	if winCheck(board):
		print "player2 wins!"
		return
	else:
		print "당신 차례입니다"
		player1(board)

board = initialize()
player1(board)