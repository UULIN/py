from multiprocessing import Queue, Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main():
    Queue()
    Queue(target=sub_task, args=('Ping',)).start()
    Queue(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main()