# coding:utf-8
import time

def job(res):
    for i in range(10):
        res.append(i*i)
        time.sleep(1)



if __name__ == "__main__":
    start_time = time.time()
    res = []
    job(res)
    print(res)
    end_time =time.time()
    print("不使用进程池所用时间为", (end_time-start_time))
