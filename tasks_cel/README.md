开启Work ，并发 启动异步命令
 celery -A celery_tasks worker -l info -P eventlet

# 启动redis客户端
redis-cli.exe

# 进入库1
命令： select 1

# 查看键值
命令：keys *

# 打印键值类型
type celery

# 获取键值的值
LRANGE celery 0 -1

# 未在celery配置文件中开启beat
1.开启worker
celery -A celery_tasks worker -l info -P eventlet
2.运行生产者
python  product_task.py


在celery配置文件中开启beat
1.开启worker
celery -A celery_tasks worker -l info -P eventlet
2.开启心跳
celery -A celery_tasks beat

