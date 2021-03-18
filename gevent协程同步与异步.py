from gevent import spawn, joinall, monkey

monkey.patch_all()

import time


def task(pid, pname):
    """
    Some non-deterministic task
    """
    time.sleep(0.5)
    print('Task %s done %s' % (pid, pname))


def synchronous():
    for i in range(10):
        task(i, "synchronous")


def asynchronous():
    g_l = [spawn(task, i, "asynchronous") for i in range(10)]
    joinall(g_l)


if __name__ == '__main__':
    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    asynchronous()