# coding:utf-8
import multiprocessing as mp
"""
    共享内存
"""


if __name__ == "__main__":
    # 第一个参数是数据类型的代码，i代表整数类型
    # 第二个参数是共享数据的值
    v = mp.Value("i", 0)

