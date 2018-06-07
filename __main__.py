#/usr/bin/python2
import collection
import text as tt
from DbUtils import MySql as Mp
def test():
    print(collection.union(('1','5','2'),('2','8')))

def readFile():
	print tt.readText('README.md')

def insert():
	mp=Mp()
	mp.excuet("insert into user(`name`,`age`) values('wengdd',233);")


if __name__ == '__main__':
    	
	insert()