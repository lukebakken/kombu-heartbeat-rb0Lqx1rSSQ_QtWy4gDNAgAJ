#!-*- coding:UTF-8 -*-
 
import sys
import argparse
import logging
import os
from oslo_config import cfg
import sys
import time
import eventlet
eventlet.monkey_patch()
import threading
 
 
import oslo_messaging
 
 
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
        self.parser.add_argument("--log",
                                 dest="log_name",
                                 default="publish.log",
                                 action="store",
                                 help="打印日志的地址")
        self.parser.add_argument("--sleep",
                                 dest="sleep_time",
                                 default="0",
                                 action="store",
                                 help="发送消息延时")
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
        self.parser.add_argument("--method",
                                 dest="method",
                                 default="call",
                                 action="store",
                                 help="call, cast, fanout")
        self.parser.add_argument("--num",
                                 dest="num",
                                 default="1",
                                 action="store",
                                 help="发送消息数量")
        result = self.parser.parse_args()
        return result
 
 
class client(object):
    def __init__(self, parser):
 
        CONF = cfg.CONF
        CONF(args=["--config-file", parser.config_file])
        # transport means how to conncet rabbitmq-server
        transport = oslo_messaging.get_transport(CONF)
        # target cover the queue, exchange, server, for example rcp.server is a queue name
        target = oslo_messaging.Target(topic=parser.topic, server='server')
        self.rpc_client = oslo_messaging.RPCClient(transport, target)
        self.method = parser.method
 
    def send(self):
        ctxt = {}
        kwargs = {"from client": "hello"}
        if self.method == "call":
            result = self.rpc_client.call(ctxt, "ADD", **kwargs)
            logging.info(result)
            return
        elif self.method == "cast":
            self.rpc_client.cast(ctxt, "ADD", **kwargs)
        else:
            fanout_obj = self.rpc_client.prepare(fanout=True)
            fanout_obj.cast(ctxt, "ADD", **kwargs)
        logging.info("send ok")
 
 
def send(client, num):
 
    th_lst = []
    for i in range(num):
        t = threading.Thread(target=client.send)
        t.setDaemon(True)
        th_lst.append(t)
 
    for th in th_lst:
        th.start()
 
    for th in th_lst:
        th.join()
 
 
if __name__ == "__main__":
    parser = Parser().get_parser()
    log_init(parser.log_name)
    client = client(parser)
    while True:
        send(client, int(parser.num))