# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
import zmq
#from zmq.devices.basedevice import ProcessDevice
#from zmq.devices import Device
#from multiprocessing import Process
#import zmq.green as zmq
import os

class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    help = 'Run the zeromq server'

    def handle(self, *args, **options):
        context = zmq.Context()
        print("Starting device...")
        pid = os.getpid()
        print("PID:{0}".format(pid))

        # Using Python Devices.
        # More info at: http://blog.pythonisito.com/2012/08/using-zeromq-devices-to-support-complex.html

        sub = context.socket(zmq.SUB)
        sub.bind("tcp://*:5555")
        sub.setsockopt(zmq.SUBSCRIBE, '')

        pub = context.socket(zmq.PUB)
        pub.bind("tcp://*:5556")

        zmq.device(zmq.FORWARDER, sub, pub)

        ## Listen for events
        #sub = context.socket(zmq.SUB)
        #sub.bind("tcp://*:5555")
        #print "Listening in port 5555 and echoing to 5556"
        #sub.setsockopt(zmq.SUBSCRIBE, '')

        ## Emit events
        #pub = context.socket(zmq.PUB)
        ##pub.connect(u'tcp://localhost:5556')
        #pub.bind("tcp://*:5556")

        #while True:
        #    message = sub.recv()
        #    pub.send(message)

