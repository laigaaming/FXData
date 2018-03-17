#-------------------------------------------------------------------------------
# Name:        fxdbopert.py
# Purpose:
#
# Author:      laigaaming
#
# Created:
# Copyright:   (c) www.laigaaming.com
# Licence:
#-------------------------------------------------------------------------------

import dbutil
import MySQLdb

def insertfxdata(db, dbtbl, scur, tcur, fxrate, cur_date):
    try:
        conn = dbutil.getfxdbconn()
        cur = conn.cursor()

        # cur.execute('create database if not exists ' + db)
        print conn.select_db(db)
        # conn.execute('create table ' + dbtbl + ' (id int, scur varchar(50), tcur varchar(50), rate double, date varchar(50))')

        fxdata = [scur, tcur, fxrate, cur_date]
        insertquery = 'insert into ' + dbtbl + ' (scur, tcur, rate, date) values (%s, %s, %s, %s)'
        cur.execute(insertquery, fxdata)

        conn.commit()
        cur.close()
        conn.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])







