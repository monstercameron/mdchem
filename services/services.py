
from API.highscore import rebuild_highscore_task
from flask_apscheduler import APScheduler


class Service():

    scheduler = APScheduler()

    def __init__(self, app):
        self.app = app

    def make(self):
        self.scheduler.init_app(self.app)

    def start(self):
        self.scheduler.start()


def make_service(app):
    service = Service(app)
    service.make()
    service.scheduler.add_job(func=rebuild_highscore_task,
                            trigger='interval',
                            minutes=60,
                            id='rebuild_highscore')
    service.start()
    return service
