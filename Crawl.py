#!/usr/bin/python
#-*- coding: utf-8 -*-

import urllib2
import re
import logging
import csv
from collections import OrderedDict


logging.basicConfig(level=logging.INFO)

count_variant=0;count_error=0;count_game=0;count_life=0;count_other=0;count_pet=0;count_pop=0;count_soccer=0;count_song=0;count_TVseries=0;count_food=0;count_movie=0;count_mugen=0;count_anime=0;count_flash=0;count_twitch=0;count_varshow=0
output=open("output.txt","wb")
#output=csv.writer(open("output.csv","wb"))
#stat=csv.writer(open("count.csv","wb"))

for beginid in range (1012500,1012680):
    userMainUrl="http://www.acfun.tv/v/ac%d" % beginid
    req = urllib2.Request(userMainUrl)
    try:
        resp = urllib2.urlopen(req)

    except Exception as ex:
        logging.info('failed to get id %d', beginid)
        count_error=count_error+1
        continue

    respHtml = resp.read()
    urlpat=re.compile(r'<title>(.*?) - ')
    match=urlpat.findall(respHtml)
    urlpat2=re.compile(r'<a id="channel-article-title".*>(.*?)</a>')
    match2=urlpat2.findall(respHtml)
#    for item2 in match2:
#        logging.info('%d: %s', beginid, item2)
#    print match2
    if match2 == ['\xe7\xbb\xbc\xe5\x90\x88']:
        count_variant=count_variant+1
    elif match2 == ['\xe6\xbc\x94\xe5\x94\xb1\xc2\xb7\xe4\xb9\x90\xe5\x99\xa8']:
        count_song=count_song+1
    elif match2 == ['\xe5\x89\xa7\xe9\x9b\x86']:
        count_TVseries=count_TVseries+1
    elif match2 == ['\xe6\xb8\xb8\xe6\x88\x8f\xe9\x9b\x86\xe9\x94\xa6']:
        count_game=count_game+1
    elif match2 == ['\xe8\x90\x8c\xe5\xae\xa0']:
        count_pet=count_pet+1
    elif match2 == ['\xe7\x94\x9f\xe6\xb4\xbb\xe5\xa8\xb1\xe4\xb9\x90']:
        count_life=count_life+1
    elif match2 == ['\xe8\xb6\xb3\xe7\x90\x83']:
        count_soccer=count_soccer+1
    elif match2 == ['\xe6\xb5\x81\xe8\xa1\x8c\xe9\x9f\xb3\xe4\xb9\x90']:
        count_pop=count_pop+1
    elif match2 == ['\xe7\x94\xb5\xe5\xbd\xb1']:
        count_movie=count_movie+1
    elif match2 == ['Mugen']:
        count_mugen=count_mugen+1
    elif match2 == ['\xe7\xbe\x8e\xe9\xa3\x9f']:
        count_food=count_food+1
    elif match2 == ['\xe5\x8a\xa8\xe7\x94\xbb\xe7\x9f\xad\xe7\x89\x87']:
        count_anime=count_anime+1
    elif match2 == ['Flash\xe6\xb8\xb8\xe6\x88\x8f']:
        count_flash=count_flash+1
    elif match2 == ['\xe5\xae\x9e\xe5\x86\xb5\xe8\xa7\xa3\xe8\xaf\xb4']:
        count_twitch=count_twitch+1
    elif match == ['\xe7\xbb\xbc\xe8\x89\xba']:
        count_varshow=count_varshow+1
    else:
        count_other=count_other+1
    for item in match:
        #item.decode('utf-8')
        print item
    for item2 in match2:
        #item2.decode('utf-8')
        print item2

    output.write("<"+item2+">"+"<"+item+">"+"\r\n")
#    output.writerow([item2,item])

ordered_fieldnames = OrderedDict([('count_variant',None),('count_error',None),('count_song',None),('count_TVseries',None),('count_game',None),('count_pet',None),('count_life',None),('count_soccer',None),('count_pop',None),('count_other',None),('count_food',None),('count_anime',None),('count_movie',None),('count_mugen',None),('count_flash',None),('count_twitch',None),('count_varshow',None)])
with open("count.csv","wb") as fou:
    stat=csv.DictWriter(fou,fieldnames=ordered_fieldnames)
    stat.writeheader()
    stat=csv.writer(fou)
    stat.writerow([count_variant,count_error,count_song,count_TVseries,count_game,count_pet,count_life,count_soccer,count_pop,count_other,count_food,count_anime,count_movie,count_mugen,count_flash,count_twitch,count_varshow])




    #for item in match:
    #    logging.info('%d: %s', beginid, item)
    #    output.writerow([item])


