#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import time

if __name__ == "__main__":
    while(1):
        #cmdstr="""netstat -anop | grep 6379"""
        cmdstr="""free | grep 'buffers/cache:' | awk -F' ' '{ print strftime("%H:%M:%S",systime())"\t",$3"\t",$4 }' >> meo.log"""
        status,output=commands.getstatusoutput(cmdstr)
        if(status == 0):
            pass
        else:
            print("error")
        time.sleep(60)
