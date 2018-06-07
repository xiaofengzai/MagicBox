import pymysql
import ConfigReader as cr

class MysqlProcessor:
    __cfg=None
    __db=None
    __cursor=None
    def __init__(self):
        self.__cfg=cr.readValues('conf.ini','mysql')
        print self.__cfg,'hah'
        self.__db = pymysql.connect(host=self.__cfg["host"],port=int(self.__cfg["port"]),user= self.__cfg["user"],password=self.__cfg["password"],db=self.__cfg["dbname"],charset='utf8' )
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
