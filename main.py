#!/bin/env python3

from urllib import request

if __name__ == '__main__':
    print('test git reflog')

    req = request.urlopen('https://afan.ml/')
    print(req.status)
    if req.status == 200:
        print(req.read().decode())

