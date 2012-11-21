# -*- coding: utf-8 -*-
from django.conf import settings

NOTIFINTIME_BACKENDS = getattr(settings, 'NOTIFICATION_BACKENDS', None)

if not NOTIFINTIME_BACKENDS:
    NOTIFINTIME_BACKENDS = (
            ('notifintime.backends.zeromq'),
            ('notifintime.backends.email'),
            )

NOTIFINTIME_GREEN = getattr(settings, 'NOTIFINTIME_GREEN', False)
