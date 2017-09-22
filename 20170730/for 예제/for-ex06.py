# coding: utf-8

# 6
i = 0
hap = 0
num1 = 0
num2 = 0
num3 = 0

num1 = int(input("시작값 입력 : "))
num2 = int(input("끝값 입력 : "))
num3 = int(input("증가값 입력 : "))

for i in range(num1, num2+1, num3) :
    hap = hap + i
    
print("%d에서 %d까지 %d씩 증가함 값의 합 : %d" % (num1, num2, num3, hap))
print("range에서 끝값이 +1 되어 있다는 것을 유의해서 보시기 바랍니다.")

