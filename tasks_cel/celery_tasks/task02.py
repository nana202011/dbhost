# -*- encoding: utf-8 -*-
'''
@File :task02.py
@Time :2022/02/16 15:19:32
@Author :苏苏
@Version :1.0
@Contact :88927069@qq.com
@Desc    :task02   
@here put the import lib
'''
import time
from celery_tasks.celery import cel
@cel.task
def send_msg(name):
    print('完成向%s发送短信任务'%name)
    time.sleep(5)
    return "短信完成"

