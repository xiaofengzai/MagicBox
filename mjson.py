import json
    
def exist(josnData,key):
    """ validate key exists in json data"""
    return key in josnData
	
def get(josnData,key):
    """ get value from json data"""
    return josnData[key] if exist(josnData,key)  else ""
	
def loadJson(jsonFile):
    """ load json file to Json String"""
    with open(jsonFile,"r") as f:
	temp=json.load(f)
	f.close()
	return temp
	
