#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import urllib2
import logging

logging.basicConfig(level=logging.INFO)

fou=open("user_info.txt","wb")


for beginid in range (1,10000):
    userMainUrl="http://www.acfun.tv/u/%d.aspx#area=post-history" %beginid
    req=urllib2.Request(userMainUrl)
    try:
        resp=urllib2.urlopen(req)
    except Exception as ex:
        logging.info ('invalid user id: %d', beginid)
        continue

    respHtml=resp.read()
    uspost=re.compile(r'post-history">.*?\((\d+)\)</a>')
    usname=re.compile(r'name: \'(.*?)\'')
    usfan=re.compile(r'#area=followers">.*?\((\d+)\)</a>')
    matchpost=uspost.findall(respHtml)
    matchname=usname.findall(respHtml)
    matchfan=usfan.findall(respHtml)
    for item in matchpost:
        print item
    for item2 in matchname:
        print item2
    for item3 in matchfan:
        print item3
    uid="<user id: %d>" %beginid
    fou.write(uid+"<user name: "+item2+">"+"<user fans: "+item3+">"+"<user posts: "+item+">"+"\r\n")

fou.close()