# -*- coding: utf-8 -*-

# p7-3 블랙잭 커플의 수 찾기

def deQuote(list):
	for i in range(0, len(list)):
		list[i] = int(list[i])

def countBJCouples(list):
	BJCouples = []								# 블랙잭 커플들의 목록 초기화

	for e in list:
		if 21 - e in list:						# 블랙잭 커플 상대를 찾은 경우
			if not [21 - e, e] in BJCouples:	# 이미 발견된 쌍이 아닌 경우
				BJCouples.append([e, 21 - e])	# 블랙잭 커플들 목록에 추가

	return len(BJCouples)						# 블랙잭 커플들의 수를 반환

x = raw_input("중복이 없는 정수의 목록을 입력하세요: ").split()
deQuote(x)

print countBJCouples(x), "쌍의 블랙잭 커플이 있습니다"