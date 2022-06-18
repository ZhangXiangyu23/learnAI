# coding:utf-8
import threading
import time

"""
    join的使用
"""


"""
    线程T1的工作
"""
def T1_job():
    print("T1 start")
    for i in range(10):
        time.sleep(0.1)
    print("T1 end")

"""
    线程T2的工作
"""
def T2_job():
    print("T2 start")
    print("T2 end")


def main():
    # 创建线程
    T1 = threading.Thread(target=T1_job, name="T1")
    # 启动线程
    T1.start()
    # 将T1进行阻塞，使T1全部执行完之后，再执行下面的脚本
    T1.join()
    T2 = threading.Thread(target=T2_job(), name="T2")
    T2.start()
    print("all end!!!")


if __name__ == "__main__":
    main()
    # 目前有几个活跃的线程
    # print(threading.active_count())
    # 各个线程的情况
    # print(threading.enumerate())