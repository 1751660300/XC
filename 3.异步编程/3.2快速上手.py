# -*- coding:utf-8 -*-
"""
1.协程函数：
    定义协程函数：async def 函数名称():
2.协程对象：
    执行协程函数()得到
注意：
    执行协程函数创建协程对象时，协程内的代码不会执行，如果想要执行协程函数内的代码，就要将协程对象交给循环事件来处理
"""
import asyncio


async def a():
    # 创建一个协程函数
    print("来呀，快活呀，反正有大把时光。。。")

# 生成一个协程对象
aClazz = a()
# 获取循环事件
loop = asyncio.get_event_loop()
loop.run_until_complete(aClazz)

# python 3.7 以上可以使用asyncio.run()方法来处理，本质上和上面的两行代码是一样的
# asyncio.run(aClazz)
