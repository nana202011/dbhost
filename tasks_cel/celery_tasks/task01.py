# -*- encoding: utf-8 -*-
'''
@File :task01.py
@Time :2022/02/16 15:11:18
@Author :苏苏
@Version :1.0
@Contact :88927069@qq.com
@Desc    :task01   
@here put the import lib
'''
import time
from celery_tasks.celery import cel

@cel.task
def send_email(res):
    print('完成向%s发送邮件任务'%res)
    time.sleep(5)
    return '邮件完成'

