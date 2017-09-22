# coding: utf-8

# 7
i = 0
dan = 0

dan = int(input(" 몇 단 ? "))

for i in range(1, 10, 1) :
    print(" %d  X  %d  =  %2d" % (dan, i, dan*i))
