# coding:utf-8


init_a = [[1, 2, 3], [4, 5, 6]]

in_x = 0
in_y = 0


# 计算坐标
def compute_coordinate(a, x, y):
    out_x = x
    out_y = y
    coordinate = []
    # 寻找行坐标
    for i in range(len(init_a)):
        row_max = init_a[in_x][in_y]
        if init_a[i][in_y] > row_max:
            out_x = i

    # 寻找列坐标
    for j in range(len(init_a[0])):
        column_max = init_a[in_x][in_y]
        if init_a[in_x][j] > column_max:
            out_y = j

    coordinate.append(out_x)
    coordinate.append(out_y)
    return coordinate



cout = len(init_a) * len(init_a[0])

# 迭代
for i in range(cout):
    s = compute_coordinate(init_a, in_x, in_y)
    print(f"第{i}次迭代完成,坐标为", (s[0], s[1]))
    print("值为", init_a[s[0]][s[1]])
    print("----------" * 10)
    in_x = s[0]
    in_y = s[1]


