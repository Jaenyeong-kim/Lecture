# -*- coding: utf-8 -*-

# prog4-3 else 사용예

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
else:
	message = "보통 미만!"
	print message

print "누구에게나 메시지를 전달했습니다"