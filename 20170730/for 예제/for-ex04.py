# coding: utf-8

# 4
i = 0
hap = 0

for i in range(1, 11, 2) :
#   print("i의 값은 {} 입니다.".format(i))
    print("i의 값은 %d입니다." % i)    
    hap = hap + i
    
print("1에서 10까지 홀수의 합 : %d" % hap)
