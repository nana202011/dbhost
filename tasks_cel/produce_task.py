# -*- encoding: utf-8 -*-
'''
@File :produce_task.py
@Time :2022/02/16 15:29:49
@Author :苏苏
@Version :1.0
@Contact :   88927069@qq.com
@Desc    :生产者-制造消息  
@here put the import lib
'''
from datetime import datetime
from time import ctime
from unittest import result
from celery_tasks.task01 import send_email
from celery_tasks.task02 import send_msg
# 时差类，设定固定时差
from datetime import timedelta


#################################################
#              异步任务                         #
#################################################
'''
#立即告知celery去执行test_celery任务，并传入一个参数
result = send_email.delay('yuan')
print(result.id)

result2= send_msg.delay('yuan')
print(result2.id)
'''

#################################################
#              定时任务                         #
#################################################
'''
#方式1
v1 = datetime(2022,2,16,16,32,00)
print(v1)
v2 = datetime.utcfromtimestamp(v1.timestamp())
print(v2)
# 含eta 定时，不含相当异步 
result = send_email.apply_async(args=['egon',],eta=v2)
print(result.id)
'''

# 方式二
ctime = datetime.now()
# 默认用utc时间
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
time_delay = timedelta(seconds=10)
# + --- 当前时间推迟10秒执行
task_time = utc_ctime+time_delay
#使用apply_async并设定时间
result = send_email.apply_async(args=['egon'],eta=task_time)
print(result.id)

