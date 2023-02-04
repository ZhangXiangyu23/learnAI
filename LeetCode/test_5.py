# coding:utf-8

used = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 记录当前数字是否可用
a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 九宫格，保存当前探索的数值


def search(m):  # m表示当前探索到了第几层
    global used
    # 解空间树探索到叶子节点(第九层)，判断该解是否符合要求
    if m == 9:
        if isOk():
            # 符合条件，输出
            output()
            print()
            # 没有遍历到叶子节点，继续深度优先遍历解空间树
        else:
            for i in range(1, 10):
                if used[i] == 0:
                    a[int(m/3)][m % 3] = i
                    used[i] = 1
                    search(m+1)
                    used[i] = 0


def isOk():
    flag = 1
    for i in range(3):
        if a[i][0] + a[i][1] + a[i][2] != 15 or a[0][i] + a[1][i] + a[2][i] != 15:
            flag = 0
            return False
    if a[0][0] + a[1][1] + a[2][2] != 15 or a[0][2] + a[1][1] + a[2][0] != 15:
        flag = 0
        return False
    if flag == 1:
        return True

# 进行输出
def output():
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(a[i][j], end="")
            else:
                print(a[i][j], end=" ")
        print()


if __name__ == "__main__":
    # 从0层开始深度优先遍历
    search(0)


