# -*- coding: utf-8 -*-

# ex6-5 평균 점수 인쇄

def average(rec):
	name = rec[0]
	avg = (int(rec[1][0]) + int(rec[1][1]) + int(rec[1][2])) / 3
	print name, "평균 =", avg 

line = raw_input("이름과 세 개의 점수: ")
lineList = line.split()
name = lineList[0]
scoresList = lineList[1:]

average([name, scoresList])