# coding:utf-8
import multiprocessing as mp
import time
import threading as th
"""
    多进程、多线程、普通方法的性能比较
"""

# 每个大约10s
def mp_job(res):
    for i in range(10000000):
        res += i**5 + i**6
    print(res)

def mt_job(res):
    for i in range(10000000):
        res += i**5 + i**6
    print(res)

def normal_job(res):
    for i in range(10000000):
        res += i ** 5 + i ** 6
    print(res)




if __name__ == "__main__":
    mp_sum = 0
    mp_start = time.time()
    process1 =mp.Process(target=mp_job, args=(mp_sum, ))
    process2 = mp.Process(target=mp_job, args=(mp_sum,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    mp_end = time.time()
    print("多进程使用时间为", (mp_end-mp_start))
    mt_start = time.time()
    mt_sum = 0
    thread1 = th.Thread(target=mt_job, args=(mt_sum, ))
    thread2 = th.Thread(target=mt_job, args=(mt_sum, ))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    mt_end = time.time()
    print("多线程使用的时间是", (mt_end-mt_start))
    normal_start = time.time()
    normal_sum = 0
    # 进行两次
    normal_job(normal_sum)
    normal_job(normal_sum)
    normal_end = time.time()
    print("普通方法使用的时间是", (normal_end-normal_start))

