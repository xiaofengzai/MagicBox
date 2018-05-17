import pymysql
import ConfigUtil as cfu

class MysqlProcessor:
    __cfg=None
    __db=None
    __cursor=None
    def __init__(self):
        self.__cfg=cfu.readValues('conf.ini','mysql')
        self.__db = pymysql.connect(self.__cfg["host"],self.__cfg["port"], self.__cfg["user"],self.__cfg["password"],self.__cfg["dbname"],charset='utf8' )
        self.__cursor = self.__db.cursor()

    def __execute(self,script):
        self.__cursor.execute(script)

    def findOne(self,script):
        self.__execute(script)
        return self.__cursor.fetchone()

    def update(self,script):
        self.__execute(script)

    def findAll(self,script):
        self.__execute(script)
        return self.__cursor.fetchall()

    def close():
        if self.__db != None:
            self.__db.close()
