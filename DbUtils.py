import pymysql
import pymssql
import xlwt
from pymongo import MongoClient
import ConfigReader as cr

class BaseDb:
    __db=None
    __cursor=None
    def __init__(self,db):
        self.__db = db
        self.__cursor = self.__db.cursor()

    def __execute(self,script):
        """ execue sql"""
        self.__cursor.execute(script)

    def findOne(self,script):
        """ query one record """
        self.__execute(script)
        return self.__cursor.fetchone()

    def excuete(self,script):
        """ insert or update """
        self.__execute(script)
        self.__db.commit()

    def findAll(self,script):
        """ query  record list """
        self.__execute(script)
        return self.__cursor.fetchall()

    def exportExcel(self,script,outFileName):
        # self.__cursor.scroll(0,mode='absolute')
        results = self.findAll(script)
        fields = self.__cursor.description
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('sheet0',cell_overwrite_ok=True)
        for field in range(0,len(fields)):
            sheet.write(0,field,fields[field][0])
        row = 1
        col = 0
        for row in range(1,len(results)+1):
            for col in range(0,len(fields)):
                sheet.write(row,col,u'%s'%results[row-1][col])
        workbook.save(r'./{}.xlsx'.format(outFileName))


    def close(self):
        if self.__db != None:
            self.__db.close()
    

class MySql(BaseDb):
    """ to connect mysql"""
    __cfg=None
    def __init__(self):
        self.__cfg=cr.readValues('conf.ini','mysql')
        self.__db = pymysql.connect(host=self.__cfg["host"],port=int(self.__cfg["port"]),user= self.__cfg["user"],password=self.__cfg["password"],db=self.__cfg["dbname"],charset='utf8' )
        BaseDb.__init__(self,self.__db)


class MSSQL(BaseDb):
    """ to connect MSSQL"""
    __cfg=None
    def __init__(self):
        self.__cfg=cr.readValues('conf.ini','sqlserver')
        self.__db = pymssql.connect(self.__cfg["host"],self.__cfg["user"],self.__cfg["password"],self.__cfg["dbname"] )
        BaseDb.__init__(self,self.__db)


class Mongo:
    """ to operate mongodb """
    def __init__(self,dbname=None):
        self.__cfg=cr.readValues('conf.ini','mongo')
        client = MongoClient(self.__cfg["host"], int(self.__cfg["port"]))
        if dbname==None:
            self.db = client[self.__cfg["dbname"]]
        else:
            self.db=client[dbname]
        self.db.authenticate(self.__cfg["user"], self.__cfg["password"])

    def getCollections(self):
        return self.db.collection_names(include_system_collections=False)

    def findOne(self,collectionName):
        return self.db[collectionName].find_one()

    def findByID(self,collectionName,id):
        return self.db[collectionName].find_one({"_id":id})

    def findAll(self,collectionName,param):
        return self.db[collectionName].find(param)

    def count(self,collectionName,param):
        return self.db[collectionName].find(param).count()

    def insertOne(self,collectionName,json):
        return self.db[collectionName].insert_one(json).inserted_id

    def insertMany(self,collectionName,json):
        return self.db[collectionName].insert_many(json).inserted_ids

    def find(self,collectionName,param,sorted):
        return self.db[collectionName].find(param).sort(sorted)

    