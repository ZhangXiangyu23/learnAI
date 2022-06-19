# coding:utf-8
import time
import multiprocessing as mp
"""
    使用多进程时，运行程序所用的时间
"""

def job1(q):
    res = 0
    for i in range(100):
        res += i + i**5 +i**8
        time.sleep(0.1)
    # 将结果放入队列中
    q.put(res)


def job2(q):
    res = 0
    for i in range(100):
        res += i + i**5 +i**8
        time.sleep(0.1)
    q.put(res)


if __name__ == "__main__":
    start_time = time.time()
    # 创建队列
    q = mp.Queue()
    # 创建进程1
    process1 = mp.Process(target=job1, args=(q,))
    # 创建进程2
    process2 = mp.Process(target=job2, args=(q,))
    process1.start()
    process2.start()
    # 通过队列获取值
    res1 = q.get()
    res2 = q.get()
    print("res1为%d,res2为%d" % (res1, res2))
    end_time = time.time()
    print("整个过程所用时间为%s" %(end_time-start_time))
