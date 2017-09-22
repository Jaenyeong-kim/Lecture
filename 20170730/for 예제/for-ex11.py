# coding: utf-8

# 10
hap = 0
i = 0

for i in range(1,101) :
    hap += i
    print("i는 {}이고, 합은 {}입니다.".format(i, hap))

    if hap >= 1000 :
        break
    
print("1~100까지 누적 합계에서 최초로 1000 이 넘는 위치 : %d" % i)
