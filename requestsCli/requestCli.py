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

args = parser.parse_args()
# What was past


def printKeyAndValue():
    return '''%s key and value: %s %s\n''' % (Colors.gray, Colors.green, value)
def printMethod():
    return '''%s method: %s %s\n''' % (Colors.gray, Colors.green, method)
def printPath():
    return '''%s path: %s %s\n''' % (Colors.gray, Colors.green, path)
def printSave():
    return '''%s Saving data of %s %s %s...\n''' % (Colors.gray, Colors.green, path, Colors.gray)
def printCopy():
    return '''%sMaking a copy of %s %s %s...\n''' % (Colors.gray, Colors.green, path, Colors.gray)

def sent():
    
    contentData = requests.get(path)
    
    if (method == 'post'):
        print(printMethod() + printPath() + printKeyAndValue())
        
    if (method == 'get'):
        print(printMethod() + printPath())
        
    if (copy):
        print(printCopy())
        copySite(args, path, openBrowser)
        print('''\n%sCopy successful!\n''' % (Colors.green))
        
    if (save):
        print(printMethod() + printPath() + printSave())
        saveContent(contentData)
        print('''\n%sSave successful!\n''' % (Colors.green))


# for each arg 
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
        if (method != 'post' and method != 'get'):
            print(Colors.red + '\nMethod not exists\n')
            
        if (args.cookies):
            cookies = True
        if (args.Content):
            content = True
        if (args.Headers):
            headers = True
    sent()
    
else:
    print(Colors.red + "path or method is undefinned or null")
        
    
# post or get
def printStatus(response):
    return '''%sStatus: %s %s''' % (Colors.white, Colors.blue, response.status_code)

def printHeaders(response):
    return '''%sHeaders: %s %s''' % (Colors.white, Colors.gray, response.headers)

def printCookies(response):
    return '''%sCookies: %s %s''' % (Colors.white, Colors.gray, response.cookies)

def printContent(response):
    return '''%sContent: %s %s''' % (Colors.white, Colors.gray, response.content)

if (method == 'get'):
    response = requests.get(path)
    print(printStatus(response))
    if (headers):
        print(printHeaders(response))
    if (cookies):
        print(printCookies(response))
    if (content):
        print(printContent(response))

if (method == 'post'):
    response = requests.post(path, data=value)
    print(printStatus(response))
    if (headers):
        print(printHeaders(response))
    if (cookies):
        print(printCookies(response))
    if (content):
        print(printContent(response))