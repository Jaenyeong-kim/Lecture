# -*- coding: utf-8 -*-

# ex5-1 네 자리 수 암호 검증		- 함수를 사용하는 버전

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

passwd = int(raw_input("사용하고자 하는 암호를 입력하세요: "))

if verify(passwd):
	print "사용할 수 있는 암호입니다"
else:
	print "사용할 수 없는 암호입니다"