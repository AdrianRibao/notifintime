# -*- coding: utf-8 -*-

class NotificationBackendBase(object):
    name = None

    def __init__(self, *args, **kwargs):
        pass

    def send(self, data, *args, **kwargs):
        raise NotImplementedError

    def receive(self, *args, **kwargs):
        raise NotImplementedError

    def subscribe(self, channel):
        """
        Subscribe the backend to a channel.

        Returns the list of channels subscribed
        """
        raise NotImplementedError
