# -*- coding: utf-8 -*-

# ex7-2 ����� Ư�� ��ġ ���� ��ü

def replaceIdx(list, i, x):
	nlist = []

	if i < 0:
		i = len(list) + i
		
	for k in range(0, len(list)):
		if k == i:
			nlist.append(x)
		else:
			nlist.append(list[k])

	return nlist

list = raw_input("����� �Է��ϼ���: ").split()
i = input("���� ��ȣ: ")
x = raw_input("��ü ��: ")

nlist = replaceIdx(list, i, x)

print "��ü �� ���:", nlist