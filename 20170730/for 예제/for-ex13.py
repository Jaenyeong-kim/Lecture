# coding: utf-8

# 13
animals = ["dog", "cat", "bird"]
print("animals의 갯수는 %d 입니다." % len(animals))

for animal in animals:    # animals == iterable
    print(animal)

print("배열의 이름을 넣으면 자동으로 0부터 시작하고, 배열내 item의 갯수만큼 실행됩니다.")