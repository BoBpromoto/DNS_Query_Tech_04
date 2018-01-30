#!/usr/bin/python
# -*- coding : cp949 -*-

# @Author L3ad0xFF
#pandas import
import pandas as pd
import csv
import os
import sys
import time
from time import gmtime, localtime, strftime
import dns.resolver
import subprocess as sub


def filecreate() :
    target_file = open("fl0ckfl0ck.csv", "w")
    column_list = ["Num","    date", "           time", "          domain name", "       ip_addr","    DNS Server IP"]
    csvWriter = csv.writer(target_file)
    csvWriter.writerow(column_list)
    target_file.close()
    print ("\nfile create Success!!")

def setCsv(num) :
    pid_num = list()
    count = num + 1
    csv_path = str(os.getcwd()) + str("/fl0ckfl0ck.csv")
    print (csv_path)
    print ("\n")
    target_File = open(csv_path, 'a', newline = '')
    qurey_list = list()
    now_date = time.strftime("%Y-%m-%d", localtime())
    now_time = time.strftime("%H:%M:%S", localtime())
    #gmt_date = time.strftime("%Y-%m-%d", gmtime())
    #gmt_time = time.strftime("%H:%M:%S", gmtime())

    domain = "fl0ckfl0ck.info"
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']

    try :
        ip_query = resolver.query(domain, 'A')
        for rdata in ip_query :
            ip_addr = rdata.address
    except :
        resolver.nameservers = ['64.6.64.6']
        ip_query = resolver.query(domain, 'A')
        for rdata in ip_query :
            ip_addr = rdata.address
            
    qurey_list = [str(" ") + str(count), str("  ") + now_date, str("  ") + now_time + str(" (GMT+9)"), str("  ") + domain, str("  ")+ ip_addr, str("    ") + str(resolver.nameservers[0])]
    print ("  ".join(qurey_list) +"\n")
    csvWriter = csv.writer(target_File)
    csvWriter.writerow(qurey_list)
    target_File.close()
    p = sub.Popen(['pidof', 'python3', 'DNS_Query.py'],stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()
    pid_num.append(output.decode('utf-8'))
    pid_num = pid_num[0].split(" ")
    print ("IF you want quit, Input the command 'kill -9 " + str(pid_num[0]) + "'")
    return count

count = 0
while True :
    start = time.time()
    if os.path.exists("fl0ckfl0ck.csv") == False :
        filecreate()
        count = setCsv(count)
        end = time.time() -start
        sleepTime = 3600 -end
        time.sleep(sleepTime)
    else :
        count = setCsv(count)
        end = time.time() - start
        sleepTime = 3600 - end
        #print (sleepTime)
        time.sleep(sleepTime)
