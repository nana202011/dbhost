定位到celerytask文件夹下
cmd  命令 （异步任务命令执行）
celery -A celery_task worker -l info

celery_task  --- 异步任务文件

切记要开启redis服务，不然会报错误"由于目标计算机积极拒绝，无法链接..." 
