from celery import Celery

app = Celery('tasks', backend='rpc', broker='amqp://worker1:killme@127.0.0.1/myvhost')

@app.task
def add(x, y):
    return x + y