# -*- encoding: utf-8 -*-
'''
@File :result.py
@Time :2022/02/16 11:25:24
@Author :苏苏
@Version :1.0
@Contact :   88927069@qq.com
@Desc    :异步结果检查
@here put the import lib
'''
from unittest import result
from celery.result import AsyncResult
from celery_task import cel

async_result=AsyncResult(id='6f4466f5-a095-4abf-b7a4-e53473af01d1',app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
    #将结果删除
    result.forget()
elif async_result.failed():
    print('执行失败')
elif async_result.status=="PENDING":
    print('任务等待中被执行')
elif async_result.status=="RETRY":
    print("任务异常后正在重试")
elif  async_result.status=="STARTED":
    print('任务已经开始被执行')
