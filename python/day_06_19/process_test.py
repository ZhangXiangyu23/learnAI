# coding:utf-8
# 导入多进程的包，并重命名为mp
import multiprocessing as mp


# 主要工作
def p1():
    print("zxy")


if __name__ == "__main__":
    # 创建新进程
    new_process = mp.Process(target=p1, name="p1")
    # 启动这个进程
    new_process.start()
    # 阻塞该进程
    new_process.join()