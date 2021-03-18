from gevent import monkey

monkey.patch_all()  # 识别线程中的所有阻塞
import gevent
import time


def eat(name):
    print('%s eat 1' % name)
    time.sleep(2)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    time.sleep(2)
    print('%s play 2' % name)


if __name__ == '__main__':
    g1 = gevent.spawn(eat, "fans")
    g2 = gevent.spawn(play, name="ball")
    gevent.joinall([g1, g2])
    print("主")
