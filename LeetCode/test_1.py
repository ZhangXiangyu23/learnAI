# coding:utf-8

# 交换第0个数和第i个数
def swap(data, i):
    term = data[i]
    data[i] = data[0]
    data[0] =term
    return data


def p_1(data):
    for i in range(len(data)):
        swap(data, i)
        print(data)


a = [1, 2, 3]
p_1(a)

