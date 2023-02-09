import os
import requests
import argparse

from modules.copysite import copySite
from modules.savecontent import saveContent

# Colors for CLI
from modules.colors import Colors

# Default values for arguments
method = False
path = False
value = False
key = False
cookies = False
content = False
headers = False
copy = False
openBrowser = False
save = False
times = 1

parser = argparse.ArgumentParser()

# Arguments
parser.add_argument(
    '-m',
    '--method',
    nargs='?',
    const=True,
    help='choice method')

parser.add_argument(
    '-p',
    '--path',
    nargs='?',
    const=True,
    help='insert path')

parser.add_argument(
    '-v',
    '--value',
    nargs='?',
    const=True,
    help='insert value')

parser.add_argument(
    '-k',
    '--key',
    nargs='?',
    const=True,
    help='insert key for value')

parser.add_argument(
    '-c',
    '--cookies',
    nargs='?',
    const=True,
    help='insert cookies option')

parser.add_argument(
    '-C',
    '--Content',
    nargs='?',
    const=True,
    help='insert Content option')

parser.add_argument(
    '-H',
    '--Headers',
    nargs='?',
    const=True,
    help='insert Headers option')

parser.add_argument(
    '-cp',
    '--copy',
    nargs='?',
    const=True,
    help='Copy site')

parser.add_argument(
    '-o',
    '--openBrowser',
    nargs='?',
    const=True,
    help='open site clone')

parser.add_argument(
    '-s',
    '--saveContent',
    nargs='?',
    const=True,
    help='save content')

parser.add_argument(
    '-t',
    '--times',
    nargs='?',
    const=True,
    help='how many times do you want to send the request')

args = parser.parse_args()
# What was past


# Header, Queries and Tasks Prints
def printStatus(response):
    return '''%sStatus: %s %s''' % (Colors.white, Colors.blue, response.status_code)

def printHeaders(response):
    return '''%sHeaders: %s %s''' % (Colors.white, Colors.gray, response.headers)

def printCookies(response):
    return '''%sCookies: %s %s''' % (Colors.white, Colors.gray, response.cookies)

def printContent(response):
    return '''%sContent: %s %s''' % (Colors.white, Colors.gray, response.content)

def printKeyAndValue():
    return '''%sKey and Value: %s %s''' % (Colors.gray, Colors.green, value)

def printMethod():
    return '''%sMethod: %s %s\n''' % (Colors.gray, Colors.green, method)

def printTimes():
    return '''%sTimes: %s %s\n''' % (Colors.white, Colors.green, times)

def printPath():
    return '''%sPath: %s %s''' % (Colors.gray, Colors.green, path)

def printSave():
    return '''%s[...] Saving data of %s on %s %s\saves %s...''' % (Colors.gray, path, Colors.yellow, os.getcwd(), Colors.gray)

def printCopy():
    return '''%s[...] Making a copy of %s %s %s...''' % (Colors.gray, Colors.green, path, Colors.gray)

# ---- Div ----
def div(name='???', n=25):
    print( Colors.gray +('-'*n) + name + '-'*n)
    
    
def showStatusAndVerifyArgsHeadersCookiesAndContent(response):
    if (headers):
        print(printHeaders(response))
    if (cookies):
        print(printCookies(response))
    if (content):
        print(printContent(response))


def mainExec():
    contentData = requests.get(path)

    # -------- Header [start] --------
    div('HEADER')
    if (method and method == 'post' or method == 'get'):
        print(printMethod() + printPath())
        if (method == 'post'):
            print(printKeyAndValue())
    else:
        print(Colors.red + '\n> Method not exists or not was defined\n') 
    # -------- Header [end] --------
    
    # -------- Queries [start] -------- 
    
    for i in range(1, int(times) + 1):    
        print('''[...] %s - sending requests''' % int(i))
    
        if (method == 'get'):
            response = requests.get(path)    
                
        if (method == 'post'):
            response = requests.post(path, data=value)
        
    div('TASKS')
    print(printStatus(response))
    print(printTimes())
    
    showStatusAndVerifyArgsHeadersCookiesAndContent(response)
    
    # -------- Queries [end] --------
    
    # -------- Output tasks [start] --------
    if (method and method == 'post' or method == 'get'):
        if (copy):
            print(printCopy())
            copySite(args, path, openBrowser) # task   
            print('''%s✅ Copy successful!''' % (Colors.green))
        if (save):
            print(printSave())
            saveContent(contentData) # task   
            print('''%s✅ Save successful!''' % (Colors.green))
    # -------- Output tasks [end] --------
    
# -------- Defines args and values --------
if (args.path):
    path = args.path

    if (args.saveContent):
        save = True

    if (args.copy):
        copy = True
        

    if (args.method):
        method = args.method
        
        if (args.method == 'post'):
            key = args.key
            value = {args.key: args.value}
            
        if (args.times):
            times = args.times

        if (args.cookies):
            cookies = True
        if (args.Content):
            content = True
        if (args.Headers):
            headers = True
            
    # exec final 
    mainExec()

else:
    print(Colors.red + "\n> Needs a path")