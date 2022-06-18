# coding:utf-8
import threading
import time

def stu1():
    print("stu1开始选课")
    global course
    if course > 0:
        course -= 1
        time.sleep(2)
        print("stu1选课成功,现在篮球课所剩名额为%d" % course)
    else:
        time.sleep(2)
        print("stu1选课失败，篮球课名额为0，请选择其他课程")



def stu2():
    print("stu2开始选课")
    global course
    if course > 0:
        course -= 1
        time.sleep(2)
        print("stu2选课成功,现在篮球课所剩名额为%d" % course)
    else:
        time.sleep(2)
        print("stu2选课失败，篮球课名额为0，请选择其他课程")

def stu3():
    print("stu3开始选课")
    global course
    if course > 0:
        course -= 1
        time.sleep(2)
        print("stu3选课成功")
        print("篮球课所剩名额为%d" %course)
    else:
        time.sleep(2)
        print("stu3选课失败，篮球课名额为0，请选择其他课程")


if __name__ == "__main__":
    # 篮球课名额
    course = 2
    T1 = threading.Thread(target=stu1, name="T1")
    T2 = threading.Thread(target=stu2, name="T2")
    T3 = threading.Thread(target=stu3, name="T3")
    T1.start()
    T2.start()
    T3.start()


