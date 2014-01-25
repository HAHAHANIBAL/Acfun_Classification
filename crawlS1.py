# -*- coding: utf-8 -*-

import urllib2
import re  
import logging


logging.basicConfig(level=logging.INFO)



for beginid in range (1000000,1012175):
    userMainUrl="http://www.acfun.tv/v/ac%d" % beginid

    req = urllib2.Request(userMainUrl)
    try:
        resp = urllib2.urlopen(req)

    except Exception as ex:
        logging.info('failed to get id %d', beginid)
        continue

    respHtml = resp.read()
    urlpat=re.compile(r'<title>(.*?) - 天下漫友是一家</title>', re.M);
    match=urlpat.findall(respHtml)
    for item in match:
        logging.info('%d: %s', beginid, item)
        output.write(item+"\n")


