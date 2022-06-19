# coding:utf-8
import multiprocessing as mp
import time
"""
    进程中的锁lock
"""

def job(v, num):
    for i in range(10):
        v.value += num
        print(v.value)
        time.sleep(0.2)



if __name__ == "__main__":
    # 多进程中的共享内存
    v = mp.Value("i", 0)
    # 进程1让共享变量每次加1
    process1 = mp.Process(target=job, args=(v, 1))
    # 进程2让共享变量每次加3
    process2 = mp.Process(target=job, args=(v, 3))
    process1.start()
    process2.start()
