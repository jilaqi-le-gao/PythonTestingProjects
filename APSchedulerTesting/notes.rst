scheduler种类
#################

BlockingScheduler：
    Scheduler是唯一的运行内容

BackgroundScheduler:
    在不使用任何其他框架的时候，scheduler在后台运行的情况，选这个。

AsyncIOScheduler：
    如果使用了asyncio模块，用这个

GeventSchduler：
    如果使用了Gevent模块。

TornadoSchdeuler：
    如果是窗见一个Tornaod服务器应用。



几个测试结果
=============

BlockingScheduler情况下，ThreadPoolExecutor，例子见BlockingScheduler：

    * 对于单个函数任务，不做任何配置，任何函数在同一时刻只能被调用一次。如果上一次没有结束，会报错。
    * job_defaults中的max_instances限制了单个函数被执行的上限次数。如果想限制数量，设置为1。

BackgroundScheduler与BlockingScheduler不一样在于需要程序保持运行，保证background能存在。例子见BackgrounScheduler。


特殊需求
============

* 对于函数执行完后，callback如何处理：

    add_listener，可以针对不同的event信号，设置不同的回调函数。对任务成功和任务失败进行不同的配置。
    而且还会把正常的errorprint到屏幕。这个故障捕捉应该是APSscheduler捕捉的。所以是没法程序拿到的。

* 对于调用函数，需要传递参数和获得返回值：



* 对于tornado的scheduler，如何使用：



* 对于动态管理任务，如何进行：

