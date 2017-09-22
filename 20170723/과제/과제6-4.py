# -*- coding: utf-8 -*-

# p6-4 주민번호로부터 생년월일 출력

def getBirthday(ssn):
	yy = ssn / 10000					# 생년
	mm = (ssn / 100) % 100				# 생월
	dd = ssn % 100						# 생일

	return [yy, mm, dd]

n = int(raw_input("주민번호 앞 6 자리: "))

list = getBirthday(n)

print "생년월일:", 1900 + list[0], list[1], list[2]