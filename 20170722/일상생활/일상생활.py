gender = ""
late = ""

gender = input("성별을 입력하세요?(M/W): ")
print("아침에 일어나기")
late = input("늦잠을 잤습니까?(Y/N): ")
if (late == "Y" or late == "y"):
    pass
else:
    print("아침 밥먹기")
print("세수하기")

if (gender == "M" or gender == "m"):
    pass
else:
    if (late == "Y" or late == "y"):
        pass
    else:
        print("화장하기")
if (late == "Y" or late == "y"):     
    print("뛰어서 등교하기")
else:
    print("여유롭게 등교하기")
