# -*- coding: utf-8 -*-

# p8-8 항공편 예약시스템 - 확장

def reserve(p, f):
	book.append([p, f])			# 예약 정보 추가

def cancel(p, f):
	book.remove([p, f])			# 예약 삭제

def flight(f):
	for item in book:
		if item[1] == f:		# 항공편이 일치하면
			print item[0]		# 승객을 인쇄

def passenger(p):
	for item in book:
		if item[0] == p:		# 승객이 일치하면
			print item[1]		# 항공편을 인쇄

book = []						# 예약장부 초기화
cmd = raw_input("command: ").split()

while cmd[0] != 'q':
	if cmd[0] == 'r':
		reserve(cmd[1], cmd[2])
	if cmd[0] == 'c':
		cancel(cmd[1], cmd[2])
	elif cmd[0] == 'f':
		flight(cmd[1])
	elif cmd[0] == 'p':
		passenger(cmd[1])

	cmd = raw_input("command: ").split()