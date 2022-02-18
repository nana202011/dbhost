# -*- encoding: utf-8 -*-
'''
@File :celery.py
@Time :2022/02/16 13:13:52
@Author :苏苏
@Version :1.0
@Contact :88927069@qq.com
@Desc    :celery配置文件 
@here put the import lib
'''
from datetime import timedelta
from xml.etree.ElementInclude import include
from celery import Celery
#celery_demo 项目名称
cel = Celery('celery_demo',
            broker='redis://127.0.0.1:6379/1',
            backend='redis://127.0.0.1:6379/2',
            #包含以下两个任务文件，去响应的py文件中找任务，对多个任务做分类
            include=[
                'celery_tasks.task01',
                'celery_tasks.task02',
                ])
# 时区
cel.conf.timezone='Asia/Shanghai'
# 是否使用UTC
cel.conf.enable_utc= False
#定时相关的任务调度器
cel.conf.beat_schedule = {
    # 名字随意起名
    'add-every-10-seconds':{
        # 执行task1下的test_celery函数
        'task':'celery_tasks.task01.send_email',
        # 每笔2秒执行一次
        # 'schedule':1.0  1秒
        # 'schedule':crontab(minute='*/1'), 每一分钟
        'schedule':timedelta(seconds=6), #6秒
        #传递参数
        'args':('张三',)
    },
    # 'add-every-12-seconds':{
    #     'task':'celery_tasks.task01.send_email',
    #     # 每年4月11号，8点42分执行
    #     'schedule':crontab(minute=42,hour=8,day_of_month=11,month_of_year=4),
    #     'args':('张三',)
    # }
}