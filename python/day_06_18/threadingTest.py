# coding:utf-8
import threading

"""
    threading练习
"""



def main():
    # # 查看目前激活的线程的数量
    # print(threading.active_count())
    # # 激活线程的具体情况
    print(threading.enumerate())
    # # 查看我主要运行的是哪一个线程
    # print(threading.current_thread())
    add_Thread()


"""
    添加一个线程
"""

# 添加的了的线程的具体工作是什么
def thread_job():
    print("this is a new thread,the num is %s" % threading.current_thread())


def add_Thread():
    # 创建一个新的线程
    added_thread = threading.Thread(target=thread_job)
    # 启动线程
    added_thread.start()



if __name__ == "__main__":
    main()
