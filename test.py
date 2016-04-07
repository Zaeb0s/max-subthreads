#!/bin/env python3
import maxthreads


# Lets say you have a function "fun" you want to run within several threads at the same time.

from time import sleep
from threading import active_count
from random import random
def fun():
    print('Active threads: ', active_count())
    sleep(random()*2)


# The following initiates a MaxThreads object with the limit set to 3
thread_limiter = maxthreads.MaxThreads(3)

# The following starts 10 threads each running the fun function.
for i in range(10):
    thread_limiter.start_thread(target=fun)


# from queue import Queue
# from threading import Thread, active_count
# from time import sleep
#
# q = Queue()
#
# def p():
#     q.get()
#     print('Got queue item')
#
#
# Thread(target=p).start()
# Thread(target=p).start()
# Thread(target=p).start()
#
# sleep(0.1)
# with q.not_full:
#     # q.not_full.acquire()
#     q.not_empty.notify()
#     # q.not_full.notify()
#     # q.not_full.release()
#
