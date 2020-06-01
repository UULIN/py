from threading import Thread
from os import getpid
from random import randint
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载程序%s' % self._filename)
        time_to_download = randint(5,10)
        sleep(time_to_download)
        print('%s下载完成，耗费了%dS' % (self._filename, time_to_download))

def main():
    start = time()
    t1 = DownloadTask('python入门')
    t1.start()
    t2 = DownloadTask('tokoyo hot')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗费了%.2f时间' % (end - start))



if __name__ == '__main__':
    main()


