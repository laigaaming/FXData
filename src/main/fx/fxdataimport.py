#-------------------------------------------------------------------------------
# Name:        fxdataimport.py
# Purpose:
#
# Author:      laigaaming
#
# Created:
# Copyright:   (c) www.laigaaming.com
# Licence:
#-------------------------------------------------------------------------------

import urllib
import json
import webbrowser
import os
import collections
import sys
import config
import datetimeutil
import fxdbopert

scurrency = ["USD", "CNY", "AUD", "HKD", "EUR", "GBP"]
tcurrency = ["USD", "CNY", "AUD", "HKD", "EUR", "GBP"]

appkey = config.appkey
sign = config.sign
format = config.format
db = config.database
dbtbl = config.db_table

cur_date = datetimeutil.current_date

def importfxdata():

    for scur in scurrency:

        for tcur in tcurrency:
            if scur!=tcur:
                # print "Scurrency is: " + scur + " and tcurrency is: " + tcur
                url = "http://api.k780.com/?app=finance.rate&scur="+scur+"&tcur="+tcur+"&appkey="+appkey+"&sign="+sign+"&format="+format
                # print url

                response = urllib.urlopen(url).read()
                # print response
                jsonresp = json.loads(response)

                if jsonresp["success"] == "1":
                    scurr = jsonresp["result"]["scur"]
                    tcurr = jsonresp["result"]["tcur"]
                    fxratenm = jsonresp["result"]["ratenm"]
                    fxrate = jsonresp["result"]["rate"]
                    updtime = jsonresp["result"]["update"]
                    print "=============================START=================================="
                    print "scurr: " + scurr
                    print "tcurr: " + tcurr
                    print "fxratenm: " + fxratenm
                    print "fxrate: " + fxrate
                    print "updatetime: " + updtime
                    fxdbopert.insertfxdata(db, dbtbl, scurr, tcurr, fxrate, cur_date)
                    print "==============================END================================="
                    print " "


                else:
                    msgid = jsonresp["msgid"]
                    msg = jsonresp["msg"]
                    print "=============================START=================================="
                    print "ERROR: "
                    print msgid
                    print msg
                    print "==============================END================================="
                    print " "

importfxdata()