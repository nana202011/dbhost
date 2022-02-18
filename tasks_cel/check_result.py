from unittest import result
from celery.result import AsyncResult
from celery_tasks.celery import cel

async_result = AsyncResult(id='d624ad09-4e7a-4972-93b0-6bffceac7b76',app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
    # 将结果删除，执行完成，结果不会自动删除
    # result.forget()
    # 无论现在是什么时候，都要终止
    #result.revoke(terminate=True)
    #如果任务还没有开始执行，那么就可以终止
    #result.revoke(terminage=False)
elif async_result.failed():
    print('执行失败')
elif async_result.status == 'PENDING':
    print('任务等待中执行')
elif async_result.status == "RETRY":
    print('任务异常后正在重试')
elif async_result.status == 'STARTED':
    print('任务已经开始被执行')