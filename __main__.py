#!/usr/bin/python2
import collection
import text as tt
from DbUtils import MySql as Mp
from DbUtils import MSSQL as Ms
from DbUtils import Mongo as Mg


def test():
    print(collection.union(('1', '5', '2'), ('2', '8')))


def readFile():
    print tt.readText('README.md')


def insert():
    mp = Mp()
    mp.excuete("insert into user(`name`,`age`) values('wengdd',233);")


def query():
    ms = Ms()
    result = ms.findAll('select * FROM Acc_Bus_BillNumber;')
    for i in result:
        print i[0], i[1]

def mongo():
    mg=Mg()
    print mg.getCollections()

if __name__ == '__main__':

    mongo()
