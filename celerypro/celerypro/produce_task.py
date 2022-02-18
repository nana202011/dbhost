# -*- encoding: utf-8 -*-
'''
@File :produce_task.py
@Time :2022/02/16 10:18:05
@Author :苏苏
@Version :1.0
@Contact :88927069@qq.com
@Desc    :执行任务   - 生产者
@here put the import lib
'''
from unittest import result
from celery_task import send_email
from celery_task import send_msg
result = send_email.delay("yuan")
print(result.id)
result2 = send_msg.delay("alex")
print(result2.id)

