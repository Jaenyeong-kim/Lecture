# -*- coding: utf-8 -*-

# prog6-1 목록을 반환하는 함수예

def getParents():
	father = raw_input("아버지 성함은? ")
	mother = raw_input("어머니 성함은? ")

	return [father, mother]

parents = getParents()

print "부 =", parents[0]
print "모 =", parents[1]