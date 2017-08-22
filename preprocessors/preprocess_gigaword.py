#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# import tensorflow as tf


from html.parser import HTMLParser
from html.entities import name2codepoint
import os
import nltk
import sys
import getopt


class GigaWordParser(HTMLParser):
    cacheText = ""
    isTag = False
    f = None

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.f = open(file_name, "w+")

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'p':
            self.isTag = True

    def handle_endtag(self, tag):
        if tag.lower() == 'p':
            self.isTag = False
            self.cacheText = self.cacheText + '\n'
            self.f.write(self.cacheText + "\n")
            print(self.cacheText)
            self.cacheText = ''

    def handle_data(self, data):
        if self.isTag is True:
            data = data.replace('\n',' ')
            data = " ".join(nltk.word_tokenize(data))
            self.cacheText = self.cacheText + data



def loopForFile(rootDir,saveTxtDir):
    parser = GigaWordParser(saveTxtDir)
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            filename = os.path.join(root, f)
            f = open(filename, errors='ignore')
            parser.feed(f.read())


def main(argv):
    dir_file = ''
    txt_file = ''
    try:
        opts, args = getopt.getopt(argv,"d:t:",["dir_file=","txt_file="])
    except getopt.GetoptError:
        print('error')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--dir_file"):
            dir_file = arg
        elif opt in ("-t", "--txt_file"):
            txt_file = arg

    loopForFile(dir_file,txt_file)

if __name__ == '__main__':
    main(sys.argv[1:])

