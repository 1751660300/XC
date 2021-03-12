from greenlet import greenlet, GreenletExit

# 方法
'''
g = greenlet()
g.switch("123")  # 相当于send函数，用于切换协程，参数可以只写一次
'''


def c(n):
    while True:
        try:
            n = g1.switch()
            print("c---->{}".format(n))
        finally:
            print("结束")



def p():
    for i in range(1, 5):
        n = i
        print("p---->{}".format(n))
        g2.switch(n)


g1 = greenlet(p)
g2 = greenlet(c)
g2.switch(0)
# g1.switch()
print(g1.dead, g2.dead)


