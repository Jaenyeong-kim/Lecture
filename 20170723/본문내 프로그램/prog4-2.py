# -*- coding: utf-8 -*-

# prog4-2 elif 사용예

grade = raw_input("학점은? ")

if grade == 'A':
	message = "우수!"
	print message
elif grade == 'B':
	message = "양호!"
	print message
elif grade == 'C':
	message = "보통!"
	print message

print "위에 아무 메시지도 보이지 않으면 보통 미만 등급입니다"