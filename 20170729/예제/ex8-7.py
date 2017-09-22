# -*- coding: utf-8 -*-

# ex8-7 폭탄 돌리기 - 변형

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
#		print players[i], "가 게임에서 제외되었습니다"
#		sitters.append(players[i])
#		
#	survivorIdx = findLast(players, sitters, num, i)
#
#	return players[survivorIdx]				# 최종 생존자

def playGame(players, i, k):				# while ver.
	n = num = len(players)
	sitters = []							# 앉은 플레이어들

	while n > 1:
		i = findNext(players, sitters, num, i, k)
		print players[i], "가 게임에서 제외되었습니다"
		sitters.append(players[i])
		n -= 1

	survivorIdx = findLast(players, sitters, num, i)
	
	return players[survivorIdx]				# 최종 생존자

players = raw_input("플레이어들을 빙둘러선 순서로 입력하세요: ").split()
i = input("시작 위치를 0 이상의 숫자로 입력하세요: ")
k = input("간격을 몇 사람으로 할까요? ")

survivor = playGame(players, i, k)

print "최종 생존자:", survivor