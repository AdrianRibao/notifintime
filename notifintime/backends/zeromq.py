# -*- coding: utf-8 -*-
from notifintime.backends.base import NotificationBackendBase
from notifintime.conf import NOTIFINTIME_GREEN

if NOTIFINTIME_GREEN:
    import zmq.green as zmq
else:
    import zmq

class ZeroMQBackend(NotificationBackendBase):
    name = 'zeromq'

    def __init__(self, *args, **kwargs):
        super(ZeroMQBackend, self).__init__(*args, **kwargs)
        self.pub_url = u'tcp://localhost:5555'
        self.receiver_url = u'tcp://localhost:5556'
        self.channels = []

    def send(self, data, *args, **kwargs):
        """
        Sends the data through the channels if they are defined. It broadcast
        the data if the channel list is empty.
        """

        context = zmq.Context()
        pub = context.socket(zmq.PUB)
        pub.connect(self.pub_url)

        if self.channels:
            for channel in self.channels:
                processed_data = u'%s %s' % (channel, data)
                pub.send_unicode(processed_data)
        else:
                processed_data = u'%s' % (data)
                pub.send_unicode(processed_data)

    def receive(self, *args, **kwargs):

        context = zmq.Context()
        receiver = context.socket(zmq.SUB)
        receiver.connect(self.receiver_url)

        if self.channels:
            for channel in self.channels:
                receiver.setsockopt(zmq.SUBSCRIBE, str(channel))
            channel, message = receiver.recv_unicode().split(' ', 1)
        else:
            receiver.setsockopt(zmq.SUBSCRIBE, '')
            message = receiver.recv_unicode()
        
        return message

    def subscribe(self, channel):
        self.channels.append(channel)
