# 변수내용 출력하기

# STEP7 - 안내문을 보여주고 변수로 년,월,일을 입력받아 보여주기
year = int(input("이번 년도를 입력하세요: ")) #변수입력값은 숫자
month = int(input("이번 월을 입력하세요: ")) #변수입력값은 숫자
day = int(input("오늘날짜를 입력하세요: ")) #변수입력값은 숫자
print("오늘날짜를  YYYYMMDD로 표현하면 %04d%02d%02d 입니다." % (year, month, day))

