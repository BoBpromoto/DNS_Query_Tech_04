#!/usr/bin/sh

# @Ahthor L3ad0xFF

import os
import sys

try :
    os.system("nohup python3 DNS_Query.py &")
except :
    print ("Can't run DNS_Query.py")
