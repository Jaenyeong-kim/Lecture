# -*- coding: utf-8 -*-

# ex6-4 평균 점수로부터 합격 여부를 판정

def average(slist):
	return (int(slist[0]) + int(slist[1]) + int(slist[2])) / 3

scores = raw_input("세 개의 점수: ")
scoresList = scores.split()

avg = average(scoresList)

if (avg >= 60):
	print "합격입니다"
else:
	print "불합격입니다"