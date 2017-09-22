# -*- coding: utf-8 -*-

# test_family.py
# 
# 다음의 patientlist, norecordlist 목록 및
# f(p), m(p) 함수의 반환값은 모두 가상의 가계에 대한 데이터임

patientlist = ['C', 'F', 'J', 'O']
norecordlist = ['H', 'I', 'K', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']

def patient(p):
	if p in patientlist:
		return True
	else:
		return False
	
def record(p):
	if p in norecordlist:
		return False
	else:
		return True

def f(p):
	if p == 'A':
		return 'B'
	if p == 'B':
		return 'D'
	if p == 'C':
		return 'F'
	if p == 'D':
		return 'H'
	if p == 'E':
		return 'J'
	if p == 'F':
		return 'L'
	if p == 'G':
		return 'N'
	if p =='J':
		return 'P'
	if p == 'L':
		return 'R'
	if p == 'M':
		return 'T'
	if p == 'O':
		return 'V'

def m(p):
	if p == 'A':
		return 'C'
	if p == 'B':
		return 'E'
	if p == 'C':
		return 'G'
	if p == 'D':
		return 'I'
	if p == 'E':
		return 'K'
	if p == 'F':
		return 'M'
	if p == 'G':
		return 'O'
	if p == 'J':
		return 'Q'
	if p == 'L':
		return 'S'
	if p == 'M':
		return 'U'
	if p == 'O':
		return 'W'