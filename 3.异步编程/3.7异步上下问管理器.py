# -*- coding:utf-8 -*-
"""
1.此对象通过定义__aenter__()和__aexit__()方法来对async with语句中的环境进行控制
"""
import asyncio


class AsyncWith(object):
    def __init__(self, conn):
        self.conn = conn

    async def doSome(self):
        # 异步操作数据库
        return "666"

    async def __aenter__(self):
        # 连接数据库
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库连接
        await asyncio.sleep(1)


async def fun():
    async with AsyncWith(1) as f:
        res = await f.doSome()
        print(res)


asyncio.run(fun())
