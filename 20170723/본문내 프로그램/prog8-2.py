# -*- coding: utf-8 -*-

# prog8-2 특정 명령 코드가 입력될 때까지 무한 반복

code = raw_input("어떤 거래를 원하세요(d, w, i, q)? ")

while code != 'q':
	print "입력하신 거래 코드는", code, "입니다"
#	service(code)					# 서비스 함수
	code = raw_input("어떤 거래를 원하세요(d, w, i, q)? ") 

print "안녕히 가세요"