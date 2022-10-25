import os
import socket

name = input('Write your name here: ')

def hst():
    if name == 'luci':
        return socket.gethostname()
    return 'just nothing'

print('hi, {}. How are you?'.format(name))
print('[...] Waiting a little more, please')
input('Alrigth, press any key for continue... {}'.format(hst()))
