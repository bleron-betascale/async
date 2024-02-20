from celery import Celery
import asyncio
from celery import Task
from celery.schedules import crontab


app = Celery('celery_app',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

class AsyncioTask(Task):
    def run(self, *args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(self.async_run(*args, **kwargs))
        loop.close()

    async def async_run(self, *args, **kwargs):
        await asyncio.sleep(1)
        print('Task running...')
        await asyncio.sleep(5)
        print('Task finished')


app.register_task(AsyncioTask())


app.conf.beat_schedule = {
    'run-every-5-minutes': {
        'task': 'celery_app.AsyncioTask',
        'schedule': crontab(minute='*/5'),
    },
}