#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by eeliu at 10/16/19

import sys,os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('./helloworld'))

from PHPAgent import PHPAgentConf
from PHPAgent.FrontAgent import FrontAgent
from Common import *
import helloworld_pb2_grpc, helloworld_pb2


import grpc

channel= grpc.insecure_channel('localhost:50051')

def handleAgentPacket(client,type,str):
    '''

    :param str str:
    :return:
    '''

    TCLogger.debug("%d,%s",type,str)

    stub = helloworld_pb2_grpc.GreeterStub(channel)

    def process_response(future):
        print(future.result().message)

    call_future = stub.SayHello.future(helloworld_pb2.HelloRequest(name='you'))
    call_future.add_done_callback(process_response)


if __name__ == '__main__':

    ac = PHPAgentConf(CAConfig)
    agent = FrontAgent(ac, handleAgentPacket)
    agent.start()

    from gevent.event import Event
    import gevent,signal
    evt = Event()

    gevent.signal(signal.SIGQUIT, evt.set)
    gevent.signal(signal.SIGTERM, evt.set)
    gevent.signal(signal.SIGINT, evt.set)

    evt.wait()
