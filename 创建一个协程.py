# 迭代器 实现了__iter__()方法和__next__() 方法 能够被for循环

# 生成器 实际上是一个迭代器，使用yield返回一个迭代器

import sys
import time


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


# 协程
# 他也是使用yield来返回值，并且记录当前的运行状态
# 使用yield和send来实现协程（生产者和消费者）


def consume():
    r = ""
    while True:
        n = yield r
        if not n:
            return
        print('[consumer] consuming %s...' % n)
        time.sleep(1)
        r = 'well received'


def produce(c):
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[producer] producing %s...' % n)
        r = c.send(n)
        print(' [producer] consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consume()
    produce(c)
