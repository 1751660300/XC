# -*- coding:utf-8 -*-
"""
1.可以向事件循环中添加多个任务
    Task用于并发调度协程，可以通过async.create_task()的方式来创建Task对象，这样可以让协程加入事件循环中等待被调度执行，
    除了使用async.create_task()来创建Task对象外，还可以使用底层的loop.create_task()或ensure_future()函数来创建。
    不建议手动实例化Task对象
2.task对象存在的意义
    完成并发操作
3.asyncio.wait(task_list)
    等待task对象列表中的task对象都返回结果后再向下执行代码
4.如果task列表中存放的是协程对象的话，会在内部先创建task对象，再放入事件循环loop中
"""
import asyncio


async def fun():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "fun"


async def main():
    task_list = [
        asyncio.create_task(fun(), name="1"),
        asyncio.create_task(fun(), name="2")
    ]
    done, pending = await asyncio.wait(task_list)
    print(done, pending)


asyncio.run(main())
