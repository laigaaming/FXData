#-------------------------------------------------------------------------------
# Name:        dbutil.py
# Purpose:
#
# Author:      laigaaming
#
# Created:
# Copyright:   (c) www.laigaaming.com
# Licence:
#-------------------------------------------------------------------------------

import MySQLdb as mdb

mdbconfig = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'charset': 'utf8'
}

def getfxdbconn():

    try:
       conn = mdb.connect(**mdbconfig)
       return conn

    except mdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
