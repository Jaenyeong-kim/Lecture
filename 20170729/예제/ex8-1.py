# -*- coding: utf-8 -*-

# ex8-1 사용 가능한 암호가 입력될 때까지 무한 반복

def verify(passwd):
	p1 = (passwd / 1000) % 10	# 첫번째 숫자 뽑아내기
	p2 = (passwd / 100) % 10	# 두번째 숫자 뽑아내기
	p3 = (passwd / 10) % 10		# 세번째 숫자 뽑아내기
	p4 = (passwd / 1) % 10		# 네번째 숫자 뽑아내기

	goodPasswd = True

	if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
		goodPasswd = False
	elif p1 + 1 == p2 and p2 + 1 == p3 and p3 + 1 == p4:
		goodPasswd = False
	elif p1 - 1 == p2 and p2 - 1 == p3 and p3 - 1 == p4:
		goodPasswd = False

	return goodPasswd

n = int(raw_input("사용할 네 자리 수 암호를 입력하세요: "))

while not verify(n):
	print "사용할 수 없는 암호입니다"
	n = int(raw_input("사용할 네 자리 수 암호를 입력하세요: "))

print "사용할 수 있는 암호입니다"