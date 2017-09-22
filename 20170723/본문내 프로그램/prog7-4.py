# -*- coding: utf-8 -*-

# prog7-4 for 반복문 사용예

years = range(2000, 2017)

for y in years:
	if y % 4 == 2:
		years[y - 2000] = '*'

print years