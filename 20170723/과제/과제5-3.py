# -*- coding: utf-8 -*-

# p5-3 암호 확인

def verifyTwo(two):					# 두 숫자로 구성된 수가 암호 두 숫자와 일치하는지 여부 검사
	Password = int("0527")			# 가상 암호 설정

	return two == Password / 100	# 주어진 두 숫자와 암호의 앞 두 숫자가 일치하는지 여부를 반환

passTwo = int(raw_input("암호의 앞 두 자리를 입력하세요: "))

if verifyTwo(passTwo):
	print "암호가 일치합니다"
else:
	print "암호가 일치하지 않습니다"