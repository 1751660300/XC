# -*- coding:utf-8 -*-
"""
1.await + （协程对象，Future，Task --> io流耗时对象）
2.使用await 关键字会阻塞程序继续执行，直到耗时对象有了返回结果后才会继续执行
"""
import asyncio
flag = 0


async def fun():
    global flag
    print("start: 开始执行耗时函数")
    await asyncio.sleep(2)
    print("end: 耗时函数执行完毕")
    flag += 1
    return flag


async def fun1():
    print("开始执行第一个耗时函数")
    response = await fun()
    print(response)
    print("开始执行第二个耗时函数")
    response2 = await fun()
    print(response2)


asyncio.run(fun1())
