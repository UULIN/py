from time import time
from multiprocessing import Process, Queue
from random import randint


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processes = []

    num_list = [x for x in range(0,10000000)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler, args=(num_list[index:index + 1250000], result_queue))
        index += 1250000
        processes.append(p)
        p.start()
    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()


    end = time()

    print(total)
    print('the time is %.3f' % (end - start))

if __name__ == '__main__':
    main()