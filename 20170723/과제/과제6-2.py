# -*- coding: utf-8 -*-

# p6-2 ��Ͽ� �±� �ޱ�

def putTag(list):
	list.append(len(list))			# list�� �ǳ��� �±� ����
	
list = raw_input("����� �Է��ϼ���: ").split()
putTag(list)

print "�±׵� �����", list, "�Դϴ�."