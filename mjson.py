imoprt json

def exist(josnData,key):
	return key in josnData
	
def get(josnData,key):
	return josnData[''+key+''] if exist(josnData,key)  else ""
	
def loadJson(jsonFile,encoding='UTF-8'):
	with open(jsonFile,"r",encoding) as f:
		temp=json.load(f)
		f.close()
		return temp
	
