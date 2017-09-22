# -*- coding: utf-8 -*-

# ex8-6 폭탄 돌리기

def findNext(n, i, k):
	i = (i + k) % n

	return i

#def playGame(players, i, k):			# for ver.
#	num = len(players)
#
#	for n2 in range(0, num - 1):
#		n = num - n2					# n은 역순범위(num ~ 2) 반복
#		i = findNext(n, i, k)
#		print players[i], "가 게임에서 제외되었습니다"
#		del players[i]
#		i = (n - 1 + i - 1) % (n - 1)	# 새로운 진행점
#
#	return players[0]					# 최종 생존자

def playGame(players, i, k):			# while ver.
	n = len(players)

	while n > 1:
		i = findNext(n, i, k)
		print players[i], "가 게임에서 제외되었습니다"
		del players[i]
		n -= 1
		i = (n + i - 1) % n				# 새로운 진행점
		
	return players[0]					# 최종 생존자

players = raw_input("플레이어들을 빙둘러선 순서로 입력하세요: ").split()
i = input("시작 위치를 0 이상의 수로 입력하세요: ")
k = input("간격을 몇 사람으로 할까요? ")

survivor = playGame(players, i, k)

print "최종 생존자:", survivor