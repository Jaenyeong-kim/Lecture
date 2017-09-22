# -*- coding: utf-8 -*-

# p8-6 두 목록의 유사성 검사

def existIn(a, b):							# 목록 a의 모든 원소가 목록 b에도 존재하는지 여부 검사
	i = 0									# a의 첫 원소를 현재 검사 대상 원소로 설정

	while i < len(a) and a[i] in b:			# a를 벗어나지 않으면서 현재 검사 대상 원소가 b에 존재하는 동안 반복
		i += 1								# 다음 원소를 현재 검사 대상 원소로 설정
	
	if i == len(a):							# a에 대한 검사를 모두 마치고 하나 초과한 경우
		return True							# a의 모든 원소가 b에도 존재한다고 결정
	else:
		return False						# 그렇지 않다고 결정

def similar(A, B):							# 목록 A, B가 유사한지 여부 검사
	return existIn(A, B) and existIn(B, A)	# A의 모든 원소가 B에 존재하며
											# B의 모든 원소가 A에 존재하는지 여부를 반환

x = raw_input("첫번째 목록 원소들을 입력하세요: ").split()
y = raw_input("두번째 목록 원소들을 입력하세요: ").split()

if similar(x, y):
	print "두 개의 목록은 유사합니다"
else:
	print "두 개의 목록은 유사하지 않습니다"