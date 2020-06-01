from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('启动下载进程,进程号[%s]' % getpid())
    print('开始下载程序%s' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成，耗费了%dS' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('python入门',))
    p1.start()
    p2 = Process(target=download_task, args=('tokoyo hot',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共耗费了%.2f时间' % (end - start))



if __name__ == '__main__':
    main()


