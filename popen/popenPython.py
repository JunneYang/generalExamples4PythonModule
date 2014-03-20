#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging
import datetime
import time

cmd ="""ps -ef | grep import_poi |  grep -v grep | wc -l"""
logging.basicConfig(filename='time.log', format="%(levelname)-10s %(asctime)s %(name)s %(message)s", level=logging.DEBUG)

#使用popen调用系统shell命令监控简称状态，进程停止，打印系统时间
while 1:
    ps=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    ps.wait()
    RetStdOut,RetStdError=ps.communicate()
    print("RetStdOut:"+RetStdOut)

    if(RetStdOut == '0'):
        strTime=datetime.datetime.now()
        logging.debug(strTime)
        break
    time.sleep(10)
