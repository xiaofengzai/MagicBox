import json
    
def exist(josnData,key):
    return key in josnData
	
def get(josnData,key):
    return josnData[key] if exist(josnData,key)  else ""
	
def loadJson(jsonFile):
    with open(jsonFile,"r") as f:
	temp=json.load(f)
	f.close()
	return temp
	
