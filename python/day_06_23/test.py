# coding:utf-8

for i in range(100, 1000):
    # 个位
    a = i % 10
    # 十位
    b = (i // 10) % 10
    # 百位
    c = i // 100
    sum = a ** 3 + b ** 3 + c ** 3
    if sum == i:
        print(i)