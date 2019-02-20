#!-*- coding:UTF-8 -*-
import argparse
import eventlet
import logging
import os
import sys
import time
from oslo_config import cfg
num = 0
import threading
import oslo_messaging
eventlet.monkey_patch()

def log_init(log_name, filemode='w'):
    logging.basicConfig(filename=os.path.join(os.getcwd(), log_name), level=logging.DEBUG, filemode=filemode,
                        format='%(asctime)s - %(levelname)s: %(message)s')


class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def get_parser(self):
        self.parser.add_argument('-v', '--version',
                                 action='version',
                                 version='%(prog)s 1.0')
        self.parser.add_argument("--no_sync",
                                 dest="no_sync",
                                 action="store_true",
                                 help="")
        self.parser.add_argument("--log",
                                 dest="log_name",
                                 default="consumer.log",
                                 action="store",
                                 help="打印日志的地址")
        self.parser.add_argument("--sleep",
                                 dest="sleep_time",
                                 default="0",
                                 action="store",
                                 help="消息处理延时")
        self.parser.add_argument("--conf",
                                 dest="config_file",
                                 default="rpc-net.conf",
                                 action="store",
                                 help="配置信息")
        self.parser.add_argument("--topic",
                                 dest="topic",
                                 default="rpc",
                                 action="store",
                                 help="topic")
        self.parser.add_argument("--route_key",
                                 dest="routing_key",
                                 default=None,
                                 action="store",
                                 help="routing_key")
        self.parser.add_argument("--queue_name",
                                 dest="queue_name",
                                 default=None,
                                 action="store",
                                 help="queue_name")
        self.parser.add_argument("--exchange",
                                 dest="exchange",
                                 default=None,
                                 action="store",
                                 help="exchange")
        self.parser.add_argument("--num",
                                 dest="num",
                                 default=1,
                                 action="store",
                                 help="num of server")
        self.parser.add_argument("--server",
                                 dest="server",
                                 default="server",
                                 action="store",
                                 help="server name")

        result = self.parser.parse_args()
        return result


class TestEndpoint(object):
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time

    def ADD(self, ctxt, **kwarg):
        global num
        time.sleep(self.sleep_time)
        first_time = int(time.time())
        num = num + 1
        while True:
            now_time = int(time.time())
            diff_time = now_time - first_time
            if diff_time < 70:
                num += 1
            else:
                break
        numstr = 'Hello World:' + str(num)
        logging.info(numstr)
        return {"result": 0, "message": numstr}


class server(object):
    def __init__(self, parser, server_name):
        CONF = cfg.CONF
        CONF(args=["--config-file=%s" % parser.config_file])
        # endpoints means rpc method handler
        self.endpoints = [TestEndpoint(int(parser.sleep_time)), ]
        # transport means how to conncet rabbitmq-server
        self.transport = oslo_messaging.get_transport(CONF)
        # target means how to send messages
        self.target = oslo_messaging.Target(topic=parser.topic,
                                            server=server_name)
                                            #routing_key=parser.routing_key,
                                            #queue_name=parser.queue_name)
        # genarator server.
        self.server = oslo_messaging.get_rpc_server(self.transport, self.target,
                                                    self.endpoints, executor='eventlet')

    def start(self):
        self.server.start()
        while True:
            time.sleep(1)

def start_server(parser,server_name):
    s = server(parser,server_name)
    s.start()

if __name__ == "__main__":
    parser = Parser().get_parser()
    log_init(parser.log_name)
    num = int(parser.num)
    lst = []

    for i in range(num):
        if parser.tf_queue_name:
            server_name = parser.server + str(i)
        t=threading.Thread(target=start_server, args=(parser,server_name))
        t.setDaemon(True)
        lst.append(t)
    for t in lst:
        t.start()
    for t in lst:
        t.join()

