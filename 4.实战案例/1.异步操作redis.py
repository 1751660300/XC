# -*- coding:utf-8 -*-
"""
1.在使用python代码操作redis时，连接/操作/断开都是网络io操作，如果在这时使用异步，就会提高并发
2.要完成异步操作redis需要安装一个支持异步操作redis的模块
    pip install aioredis


"""