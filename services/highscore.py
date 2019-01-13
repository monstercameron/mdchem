from config.config import scheduler
from API.highscore import rebuild_highscore_task

scheduler.add_job(func=rebuild_highscore_task,
                        trigger='interval',
                        seconds=10,
                        id='rebuild_highscore')


# scheduler.add_job(func=rebuild_highscore_task,
#                         trigger='interval',
#                         minutes=60,
#                         id='rebuild_highscore')
