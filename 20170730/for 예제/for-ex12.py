# coding: utf-8

# 12
animals = ["dog", "cat", "bird", "koala", "bird", "cat"]
print("animals�� ������ %d �Դϴ�." % len(animals))

for i in range(len(animals)):  # 0, 1, 2, 3
    print("i�� {}".format(i))
    animal = animals[i]
    print(animal)