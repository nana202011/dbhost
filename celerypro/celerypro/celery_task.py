# -*- encoding: utf-8 -*-
'''
@File :celery_task.py
@Time :2022/02/16 10:17:13
@Author :苏苏
@Version :1.0
@Contact :   88927069@qq.com
@Desc    :异步任务   -- 消费者
@here put the import lib
'''


import celery
import time
backend= 'redis://127.0.0.1:6379/1'
broker='redis://127.0.0.1:6379/2'
#celery 实例对象
cel = celery.Celery('test',backend=backend,broker=broker)
@cel.task
def send_email(name):
    print('向%s发送邮件...'%name)
    time.sleep(5)
    print('向%s发送邮件完成'%name)
    return 'ok'

@cel.task
def send_msg(name):
    print('向%s发送短信...'%name)
    time.sleep(5)
    print('向%s发送短信完成'%name)
    return 'ok'