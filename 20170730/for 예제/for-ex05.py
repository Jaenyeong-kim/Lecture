# coding: utf-8

# 5
i = 0
hap = 0
num = 0

num = int(input("값 입력: "))

for i in range(1, num+1, 2) :
    hap = hap + i
    
print("1에서 %d까지 홀수의 합 : %d" % (num, hap))
