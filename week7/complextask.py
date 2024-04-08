from celery import Celery, chain

app = Celery('tasks', backend='rpc', broker='amqp://worker1:killme@127.0.0.1/myvhost')

@app.task
def add(x, y):
    return x + y

@app.task
def multiply(result, z):
    return result * z

result = add.delay(4, 4)
chained_task = chain(add.s(4, 4), multiply.s(10))
chained_result = chained_task()
