import pymysql
import pymssql
import ConfigReader as cr

class BaseDb:
    __db=None
    __cursor=None
    def __init__(self,db):
        self.__db = db
        self.__cursor = self.__db.cursor()

    def __execute(self,script):
        self.__cursor.execute(script)

    def findOne(self,script):
        self.__execute(script)
        return self.__cursor.fetchone()

    def excuet(self,script):
        self.__execute(script)
        self.__db.commit()

    def findAll(self,script):
        self.__execute(script)
        return self.__cursor.fetchall()

    def close():
        if self.__db != None:
            self.__db.close()
    

class MySql(BaseDb):
    __cfg=None
    def __init__(self):
        self.__cfg=cr.readValues('conf.ini','mysql')
        self.__db = pymysql.connect(host=self.__cfg["host"],port=int(self.__cfg["port"]),user= self.__cfg["user"],password=self.__cfg["password"],db=self.__cfg["dbname"],charset='utf8' )
        BaseDb.__init__(self,self.__db)


class MSSQL(BaseDb):
    __cfg=None
    def __init__(self):
        self.__cfg=cr.readValues('conf.ini','sqlserver')
        self.__db = pymssql.connect(host=self.__cfg["host"],user= self.__cfg["user"],password=self.__cfg["password"],db=self.__cfg["dbname"],charset='utf8' )
        BaseDb.__init__(self,self.__db)