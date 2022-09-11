import requests
import argparse

method = 'get'
path = 'http://google.com'
data = "defaultValue"
key = "defaultValue"

parser = argparse.ArgumentParser()

parser.add_argument(
    '-m',
    '--method',
    nargs='?',
    help='choice method')

parser.add_argument(
    '-p',
    '--path',
    nargs='?',
    help='insert path')

parser.add_argument(
    '-d',
    '--data',
    nargs='?',
    help='insert data')

parser.add_argument(
    '-k',
    '--key',
    nargs='?',
    help='insert key for data')


args = parser.parse_args()


class Colors:
    gray = '\x1b[90m'
    red = '\x1b[91m'
    green = '\x1b[92m'
    yellow = '\x1b[93m'
    blue = '\x1b[94m'
    pink = '\x1b[95m'
    white = '\x1b[97m'


def sent():
    print(
        '''
%s method: %s %s            
%s path: %s %s'''
        % (
            Colors.gray, Colors.green, method,
            Colors.gray, Colors.green, path,
        ))


if (args.method and args.path):
    method = args.method
    path = args.path
    key = args.key
    data = {args.key: args.data}

    if (method != 'post'
            and method != 'get'):
        print('{}Method not exists'.format(Colors.red))
    else:
        sent()

        if (method == 'get'):
            response = requests.get(path)
            print(
                '''
%sStatus: %s %s
%sHeaders: %s %s
''' %
                (
                    Colors.white, Colors.blue, response.status_code,  # status
                    Colors.white, Colors.gray, response.headers  # content text
                ))
        elif (method == 'post'):
            response = requests.post(path, data=data)
            print(
                '''
%sStatus: %s %s
%sHeaders: %s %s
            ''' %
                (
                    Colors.white, Colors.blue, response.status_code,  # status
                    Colors.white, Colors.gray, response.headers  # content text
                ))
