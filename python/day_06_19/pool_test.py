# coding:utf-8
import multiprocessing as mp
import time
"""
    进程池pool的使用
"""

def job(x):
    time.sleep(1)
    return x*x;


if __name__ == "__main__":
    start_time = time.time()
    # Pool参数不写的话，默认是使用该电脑的所有核。写上参数就是指定具体用几个核
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)
    end_time = time.time()
    print("所用时间为", (end_time-start_time))

    # # 只使用一个核去运算
    # res = pool.apply_async(job, (2,))
    # print(res.get())
    #
    # # 多核进行运算
    # mult_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # print([res.get() for res in mult_res])