# coding:utf-8
import threading
import time
"""
    多线程中的锁
"""

def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        time.sleep(0.2)
        print("job1", A)
    lock.release()

def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        time.sleep(0.2)
        print("job2", A)
    lock.release()




if __name__ == '__main__':
    A = 0
    lock = threading.Lock()
    T1 = threading.Thread(target=job1, name="T1")
    T2 = threading.Thread(target=job2, name="T2")
    T1.start()
    # T1.join()
    T2.start()
    print("-----------------------",threading.active_count())


