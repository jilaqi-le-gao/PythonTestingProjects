from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
import datetime
import os
import time


def say_hello():
    print('Tick! The start time is: %s' % datetime.datetime.now())
    time.sleep(10)
    print('Tick! The end time is: %s' % datetime.datetime.now())


def another_hello():
    print('Another Tick! The start time is: %s' % datetime.datetime.now())
    time.sleep(5)
    print('Another Tick! The end time is: %s' % datetime.datetime.now())


if __name__ == '__main__':
    executor = {
        'default': ThreadPoolExecutor(10),
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3  # 这里是限制单个函数能被执行的次数上限。
    }
    scheduler = BackgroundScheduler(executor=executor, job_defaults=job_defaults)
    scheduler.add_job(say_hello, 'interval', seconds=3)
    scheduler.add_job(another_hello, 'interval', seconds=3)
    scheduler.start()

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()