# -*- coding: utf-8 -*-

# prog5-14 값을 반환하는 함수예

def getCode():
	print "원하는 거래번호를 선택하세요"
	print "	1 입금"
	print "	2 출금"
	print "	3 조회"

	code = input("거래번호: ")

	return code
		
c = getCode()

print c, "번을 선택하셨습니다"