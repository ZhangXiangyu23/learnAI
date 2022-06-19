# coding:utf-8
import time
import multiprocessing as mp
"""
    不使用多进程时，运行程序所用的时间
"""


# 大约是4s
def job1():
    global res1
    for i in range(100):
        res1 += i + i**5 +i**8
        time.sleep(0.1)


# 比job1所用时间多一点
def job2():
    global res2
    for i in range(100):
        res2 += i + i**5 +i**8
        time.sleep(0.1)


if __name__ == "__main__":
    start_time = time.time()
    res1 = 0
    res2 = 0
    job1()
    job2()
    print("res1为%d,res2为%d" % (res1, res2))
    end_time = time.time()
    print("整个过程所用时间为%s" %(end_time-start_time))
