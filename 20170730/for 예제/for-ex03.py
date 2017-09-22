# coding: utf-8

# 3
i = 0
hap = 0

for i in range(1, 11, 1) :
#   print("i의 값은 {} 입니다.".format(i))
    print("i의 값은 %d입니다." % i)    
    hap = hap + i
    
print("1에서 100까지의 합 : %d" % hap)
