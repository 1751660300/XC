# -*- coding:utf-8 -*-
"""
1.什么是异步迭代器
    实现了__aiter__()和__anext__()方法的对象，__anext__()必须返回一个awaitable对象。async for会处理
    异步迭代器的__anext__()方法所返回的可等待对象，知道引发一个StopAsyncIteration异常
2.什么是异步可迭代对象
    可以在async for处理的对象，必须通过__aiter__()方法返回一个asynchronous iterator
"""
import asyncio


class Reader(object):
    def __init__(self):
        self.count = 0

    async def inc(self):
        self.count += 1
        if self.count == 100:
            return None
        else:
            return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.inc()
        if val is None:
            raise StopAsyncIteration
        return val


# 注意，async for 只能在协程函数中使用
async def mains():
    async for item in Reader():
        print(item)


if __name__ == '__main__':
    asyncio.run(mains())