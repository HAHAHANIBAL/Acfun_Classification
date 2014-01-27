#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
#Post_Info=re.compile(r'^<T\d+><P\d+><U(\d+)><O(\d+)>')
Post_Info=re.compile(r'<(.*?)><(.*?)><(.*?)><views: (.*?)>')
with open('output.txt','rb') as fin:
    for line in fin:
        m=Post_Info.search(line)
        print line
        print m.group(4)


