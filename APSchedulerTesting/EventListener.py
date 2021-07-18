from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import datetime
import os
import time
import traceback


def success_func():
    print('Tick! The start time is: %s' % datetime.datetime.now())
    time.sleep(5)
    print('Tick! The end time is: %s' % datetime.datetime.now())


def fail_func():
    print('Another Tick! The start time is: %s' % datetime.datetime.now())
    time.sleep(5)
    print('Another Tick! The end time is: %s' % datetime.datetime.now())
    raise RuntimeError


def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


if __name__ == '__main__':
    executor = {
        'default': ThreadPoolExecutor(10),
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3  # 这里是限制单个函数能被执行的次数上限。
    }
    scheduler = BlockingScheduler(executor=executor, job_defaults=job_defaults)
    scheduler.add_job(success_func, 'interval', seconds=3)
    scheduler.add_job(fail_func, 'interval', seconds=3)
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
    except:
        print('Other exception!')