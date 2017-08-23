#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import getopt
import sys

def split(origin, train, val):
    count = 0
    f = open(origin, 'rb')
    while True:
        buffer = f.read(8192 * 1024)
        if not buffer:
            break
        count += buffer.count('\n')

    train_count = count * 0.9
    val_count = count - train_count
    f.seek(0)

    train_file = open(train, 'w+')
    val_file = open(val, 'w+')

    for i, line in enumerate(f):
        if i < train_count:
            train_file.write(line)
        else:
            val_file.write(line)

    f.close()



def main(argv):
    org = ''
    tra = ''
    val = ''

    try:
        opts, args = getopt.getopt(argv,"o:t:v:",["origin_file=","train_file=","val_file"])
    except getopt.GetoptError:
        print('error')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-o", "--origin_file"):
            org = arg
        elif opt in ("-t", "--train_file"):
            tra = arg
        elif opt in ("-v", "--val_file"):
            val = arg

    split(org,tra,val)

if __name__ == '__main__':
    main(sys.argv[1:])