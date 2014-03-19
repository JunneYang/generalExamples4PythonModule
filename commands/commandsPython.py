#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands

cmdstr="""netstat -anop | grep 6379"""
status,output=commands.getstatusoutput(cmdstr)
if(status == 0):
    print output