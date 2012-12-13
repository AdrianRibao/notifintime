# -*- coding: utf-8 -*-
import inspect
from django.utils import importlib
from notifintime.conf import NOTIFINTIME_BACKENDS
from inspect import getargspec
import json

#class NotificationManager(object):
    #def __init__(self):
        #self._registry = {}

    #def register(self, name, notification):
        #"""
        #Register the notification with a given name that must be unique.
        #"""
        #if name not in self._registry:
            #self._registry[name] = notification

#manager = NotificationManager()

#class NotificationMetaclass(type):
    #def __new__(cls, name, bases, attrs):
        #new_class = super(NotificationMetaclass, cls).__new__
        #print name, attrs
        #return new_class


class NotificationBase(object):
    #__metaclass__ = NotificationMetaclass

    backends = []
    backend_instances = {}

    def __init__(self, *args, **kwargs):
        self._configure_backends()

    def build_backend_kwargs(self, args):
        kwargs = {}
        filtered_args = [arg for arg in args if arg != 'self']
        for arg in filtered_args:
            kwargs[arg] = getattr(self, arg, None)
        return kwargs

    def _configure_backends(self):
        for backend in NOTIFINTIME_BACKENDS:
            try:
                backend_module = importlib.import_module(backend)
            except:
                continue

            for item_name, item in inspect.getmembers(backend_module, inspect.isclass):
                backend_name = getattr(item, 'name', None)
                if backend_name in self.backends:
                    args, varargs, keywords, locals = getargspec(item.__init__)
                    backend_kwargs = self.build_backend_kwargs(args)
                    backend = item(**backend_kwargs)
                    self.backend_instances[backend.name] = backend

    def send(self, data, *args, **kwargs):
        for backend_name, backend in self.backend_instances.iteritems():
            backend.send(data, *args, **kwargs)

    def process_received_message(self, message):
        """
        Process the message
        """
        message = json.loads(message)
        return message

    def receive(self, backend_name, *args, **kwargs):
        backend = self.backend_instances.get(backend_name, None)
        if backend:
            message = backend.receive(*args, **kwargs)
            message = self.process_received_message(message)
            return message

    def subscribe(self, channel):
        """
        Subscribe the backend to a channel.

        Returns the list of channels subscribed
        """
        for backend_name, backend in self.backend_instances.iteritems():
            backend.subscribe(channel)
