# coding: utf-8

# 12
animals = ["dog", "cat", "bird", "koala", "bird", "cat"]
print("animals의 갯수는 %d 입니다." % len(animals))

for i in range(len(animals)):  # 0, 1, 2, 3
    print("i는 {}".format(i))
    animal = animals[i]
    print(animal)