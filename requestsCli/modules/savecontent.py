import json
import os

def saveContent(contentData):
    
    # nameOfFile = 'content'
    # currentDir = os.getcwd()
    file = open('content.json', 'w')
    file.write('{}'.format(contentData.content))
    file.encoding('utf-8')
    file.close()