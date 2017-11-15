import threading
import time

exitFlag = 0


class SeqThread (threading.Thread):  # 继承父类threading.Thread
    ''' 序列线程（线程ID，线程Name，计数器）'''

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        # self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        print_time(self.name, 10)
        print("Exiting " + self.name)


def print_time(threadName, counter=5):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(1)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = SeqThread(1, "A")
thread2 = SeqThread(2, "B")

# 开启线程
thread1.start()
thread2.start()

print("Exiting Main Thread")
