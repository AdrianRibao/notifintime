# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
import zmq
#import zmq.green as zmq

class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    help = 'Run the zeromq server'

    def handle(self, *args, **options):
        context = zmq.Context()
        print "Connecting to the server..."

        # Listen for events
        sub = context.socket(zmq.SUB)
        sub.bind("tcp://*:5555")
        print "Listening in port 5555 and echoing to 5556"
        sub.setsockopt(zmq.SUBSCRIBE, '')

        # Emit events
        pub = context.socket(zmq.PUB)
        #pub.connect(u'tcp://localhost:5556')
        pub.bind("tcp://*:5556")

        while True:
            message = sub.recv()
            pub.send(message)

