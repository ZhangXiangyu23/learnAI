# coding:utf-8
import multiprocessing as mp
import time

"""
    进程中的锁lock
"""


def job(v, num, l):
    # 加锁
    l.acquire()
    for i in range(10):
        v.value += num
        print(v.value)
        time.sleep(0.2)
    # 解锁
    l.release()


if __name__ == "__main__":
    # 创建进程锁
    l = mp.Lock()
    # 多进程中的共享内存
    v = mp.Value("i", 0)
    process1 = mp.Process(target=job, args=(v, 1, l))
    process2 = mp.Process(target=job, args=(v, 3, l))
    process1.start()
    process2.start()
