import json

def readText( file ):
  ff=open(file)
  temp=ff.read()
  ff.close()
  return temp
  
def readTextToList( file ,seperator=','):
  return readText(file).split(seperator)
  
def readTextToJSON( file):
  return json.loads(readText(file))
  
  
def difference(list1,list2):
  return list(set(list1).difference(set(list2)))
