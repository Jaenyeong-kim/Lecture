# -*- coding: utf-8 -*-

# prog7-2 for �ݺ��� ��뿹

def findGrades(scores):
	grades = [] 

	for s in scores:
		if s >= 60:
			grades.append('Pass')
		else:
			grades.append('Fail')

	return grades

scores = [89, 53, 95, 60]
print "���� =", scores

grades = findGrades(scores)
print "���� =", grades