#!/usr/bin/env python
"""
Smasher unit tests

"""
import os
import platform
import csv
import time
import datetime
import itertools
import sys
import math
import types

HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(HERE, os.pardir))

import smashWorkers 
import form_connection

def test_conn():
    c = form_connection.micro_conn("STEWARTIA")
    assert(type(c) != types.StringType)

def test_cur():
    c = form_connection.form_connection("SHELDON")
    sql = "select top 1 airtemp_mean from LTERLogger_pro.dbo.MS04311"
    c.execute(sql)
    res = c.fetchone()
    string_res = str(res)
    assert(type(string_res) == types.StringType)

def test_daterange():
    startdate = '2015-01-01 00:00:00'
    enddate = '2015-01-02 00:00:00'

    compare_s = datetime.datetime(2015,1,1,0,0)
    compare_e = datetime.datetime(2015,1,2,0,0)
    A = smashWorkers.DateRange(startdate,enddate)
    a_range = A.dr

    assert(type(a_range) == types.ListType)
    assert(2 == len(a_range))

def test_Air():
    sd = '2015-01-01 00:00:00'
    ed = '2015-01-02 00:00:00'
    A = smashWorkers.AirTemperature(sd, ed, "SHELDON")
    assert(A.entity == 1)
    assert(type(A.od.keys())==types.ListType)
    
    x_1 = 'AIRCEN01'

    if len(sorted(A.od['AIRCEN01'].keys())) > 1:
        x = sorted(A.od['AIRCEN01'].keys())[1]
    else:
        x = sorted(A.od['AIRCEN01'].keys())[0]
    print x

    print x
    print sd

    assert(datetime.datetime.strftime(x, '%Y-%m-%d %H:%M:%S')==sd)

def test_Rel():
    sd = '2015-02-01 00:00:00'
    ed = '2015-02-02 00:00:00'
    A = smashWorkers.RelHum(sd, ed, "SHELDON")
    assert(A.entity == 2)
    assert(type(A.od.keys())==types.ListType)
    x_1 = 'RELCEN01'
    x = sorted(A.od[x_1].keys())[1]
    print x
    print sd
    assert(datetime.datetime.strftime(x, '%Y-%m-%d %H:%M:%S')==sd)

def test_Dew():
    sd = '2015-02-01 00:00:00'
    ed = '2015-02-02 00:00:00'
    A = smashWorkers.DewPoint(sd, ed, "SHELDON")
    assert(A.entity == 7)
    assert(type(A.od.keys())==types.ListType)
    x_1 = sorted(A.od.keys())[0]
    x = sorted(A.od[x_1].keys())[1]
    print x
    print sd
    assert(datetime.datetime.strftime(x,'%Y-%m-%d %H:%M:%S')==sd)

if __name__ == "__main__":
    test_conn()
    test_cur()
    test_daterange()
    test_Air()
    test_Rel()
    test_Dew()
