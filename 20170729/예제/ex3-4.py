# -*- coding: utf-8 -*-

# ex3-4 몇 개의 관계 및 논리 연산 연습

print "5는 3보다 클까요? "
print "답:", 5 > 3

print "'black'과 'dark'는 같을까요? "
print "답:", 'black' == 'dark'

x = 17

print "9 < x 와 5 > x 둘 다 맞습니까?"
print 9 < x and 5 > x

print "9 < x 와 5 > x 둘 중 하나는 맞습니까?"
print 9 < x or 5 > x

print "2 + 1 ≥ 7은 거짓인가요?"
print not 2 + 1 >= 7	# 연산 우선 순위 주의