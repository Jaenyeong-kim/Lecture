# -*- coding: utf-8 -*-

# p9-4 유전성 질환 - 변형 2

from test_family import *						# 가상의 가계

def check(p):
	count = [0, 0]								# count 앞자리, 즉 p의 조상 중 남자 질환자 수를 0으로 초기화
												# count 뒷자리, 즉 p의 조상 중 여자 질환자 수를 0으로 초기화
	
	if record(p):
		if record(f(p)):						# p의 아버지 의료기록이 있는 경우
			fcount = check(f(p))				# p의 부계 중 남녀 질환자 수 fcount를 계산
			count[0] += fcount[0]				# fcount 중 남자 수를 count 앞자리에 누적
			count[1] += fcount[1]				# fcount 중 여자 수를 count 뒷자리에 누적

			if patient(f(p)):					# p의 아버지가 유전성 질환자인 경우
				count[0] += 1					# count 앞자리에 1 추가
			
		if record(m(p)):						# p의 어머니 의료기록이 있는 경우
			mcount = check(m(p))				# p의 모계 중 남녀 질환자 수 mcount를 계산
			count[0] += mcount[0]				# mcount 중 남자 수를 count 앞자리에 누적
			count[1] += mcount[1]				# mcount 중 여자 수를 count 뒷자리에 누적

			if patient(m(p)):					# p의 어머니가 유전성 질환자인 경우
				count[1] += 1					# count 뒷자리에 1 추가

	return count								# count 반환
		
p = raw_input("이름: ")							# p의 이름 입력
mySex = input("성별: (남=1, 여=2): ") - 1		# p의 성별 입력
oppositeSex = (mySex + 1) % 2					# p의 반대 성별

count = check(p)								# p가 고위험군에 속하는지 여부를 검사

if count[mySex] > count[oppositeSex] :			# p와 같은 성별의 질환자가 p와 다른 성별의 질환자 수보다 많은 경우
	print "고위험군!"
else:
	print "고위험군 아님!"