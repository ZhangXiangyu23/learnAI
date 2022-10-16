# coding:utf-8

a = []
for i in range(10):
    a.append(i)

print(a)
# 基本索引
print("第0个元素为", a[0])
# 使用负数索引
print("第-2个元素为", a[-2])
# 索引超出有效索引范围
# print(a[100])
# 基本切片
print(a[2:8])
print(a[-5:-2])
print(a[2:-1])

# 超出有效范围
print("-" * 50)
print(a[-100:100])
print(a[3:55])

# 当start在end的右边
print("-" * 50)
print(a[8:2])

# 缺省
print("-" * 50)
print(a[:5])
print(a[2:])

# 带有步长的切片
# 步长为正
print("*" * 50)
print(a[0:7:2])
print(a[::2])
print(a[:-3:2])
print(a[-100:-4:3])


# 步长为负时
print("@" * 50)
print(a[::-1])
# 为了保证取到的区间尽可能大，所以end趋向无穷小，所以会切到索引0
print(a[6::-1])
# 因为逆序切，为了保证取到的区间尽可能大，所以start会趋向于无穷大，一直切到索引4(不包含4)
print(a[:4:-2])