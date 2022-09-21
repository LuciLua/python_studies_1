from base64 import decode
import json
import os

def saveContent(contentData):
    
    # data = str(contentData.content)
    data = str(contentData.content)
    data.encode('UTF-8', 'strict')
    # with open('content.json', 'w') as write_file:
    
    file = open('content.json', 'w')
        
    # data = json.load(write_file)
        
    json.dumps(data)
    json.dumps(data, indent=2)
        
    # jsonString = json.dumps(data)
        
    file.write(data)
    file.close()
        