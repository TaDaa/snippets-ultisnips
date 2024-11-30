import json
import tokenize
import token
import io

paths = {
    "/app" : "Beacon",
	"/app/view" : "Bn.view",
	"/app/controller" : "Bn.controller",
	"/app/app" : "Bn.app",
    "/app/manager" : "Beacon.manager",
    "/app/model" : "Beacon.model",
    "/app/store" : "Beacon.store",
    "/app/mobile/custom" : "Beacon.custom",
    "/app/desktop/custom" : "Beacon.custom",
    "/app/mobile/view" : "Beacon.view",
    "/app/desktop/view" : "Beacon.view",
    "/app/mobile/controller" : "Beacon.controller",
    "/app/desktop/controller" : "Beacon.controller",
    "/app/mobile/profile" : "Beacon.profile",
    "Ext.custom" : "Ext.custom",
    "utils": "Utils",
    "/app/custom" : 'Bn.custom'
}

def namify(path):
	path = '/' + path
	lowerCasePath = path.replace('\\','/').lower()
	found = ""
	usingProp = ""
	foundDif = 9999999
	pathLen = len(path)
	for prop in paths:
		if lowerCasePath.find(prop.lower()) != -1:
			if (abs(len(prop) - pathLen) < foundDif):
				found = paths[prop]
				usingProp = prop
				foundDif = abs(len(prop) - pathLen)
	start = lowerCasePath.find(usingProp.lower())
    #return path
	return found + path[start+len(usingProp):len(path)].replace('/','.').replace('\\','.').replace('.js','')
    #return found
	#    return path[start:len(path)].replace('/','.').replace('\\','.').replace('.js','')


