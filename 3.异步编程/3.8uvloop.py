# -*- coding:utf-8 -*-
"""
1.什么是uvloop？
    asyncio事件循环的替代方案，其速度提示了2倍左右。事件循环 > 默认的事件循环
2.安装
    pip install uvloop
3.使用
    在开头添加下面语句，就会使用uvloop事件循环
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
"""
