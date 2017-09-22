# -*- coding: utf-8 -*-

# prog7-2 for 반복문 사용예

def findGrades(scores):
	grades = [] 

	for s in scores:
		if s >= 60:
			grades.append('Pass')
		else:
			grades.append('Fail')

	return grades

scores = [89, 53, 95, 60]
print "점수 =", scores

grades = findGrades(scores)
print "학점 =", grades