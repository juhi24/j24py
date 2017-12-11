# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

from celery import Celery


def make_celery(app, **kws):
    cel = Celery(app.import_name, backend=app.config['result_backend'],
                 broker=app.config['broker_url'], **kws)
    cel.conf.update(app.config)
    TaskBase = cel.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    cel.Task = ContextTask
    return cel
