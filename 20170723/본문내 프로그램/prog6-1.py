# -*- coding: utf-8 -*-

# prog6-1 ����� ��ȯ�ϴ� �Լ���

def getParents():
	father = raw_input("�ƹ��� ������? ")
	mother = raw_input("��Ӵ� ������? ")

	return [father, mother]

parents = getParents()

print "�� =", parents[0]
print "�� =", parents[1]