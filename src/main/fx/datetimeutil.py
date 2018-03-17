#-------------------------------------------------------------------------------
# Name:        datetimeutil.py
# Purpose:
#
# Author:      laigaaming
#
# Created:
# Copyright:   (c) www.laigaaming.com
# Licence:
#-------------------------------------------------------------------------------

import time

global current_date
global current_datetime

original_datetime = time.localtime(time.time())

current_date = time.strftime('%Y%m%d', original_datetime)
current_datetime = time.strftime('%Y-%m-%d %H-%M-%S', original_datetime)

print current_date