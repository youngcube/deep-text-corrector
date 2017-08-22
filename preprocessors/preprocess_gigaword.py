#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# import tensorflow as tf
# import nltk

from html.parser import HTMLParser
from html.entities import name2codepoint

# tf.app.flags.DEFINE_string("raw_data", "", "Raw data path")
# tf.app.flags.DEFINE_string("out_file", "", "File to write preprocessed data "
#                                            "to.")

# FLAGS = tf.app.flags.FLAGS

class MyHTMLParser(HTMLParser):
    insideP = False


    def handle_starttag(self, tag, attrs):
        # print('<%s>' % tag)
        if tag == 'p':
            # print(tag)
            self.insideP = True


    def handle_endtag(self, tag):
        # print('</%s>' % tag)
        if tag == 'p':
            self.insideP = False

    def handle_startendtag(self, tag, attrs):
        pass
        # print('<%s/>' % tag)

    def handle_data(self, data):
        if self.insideP is True:
            print(data)


    def handle_comment(self, data):
        pass
        # print('<!--', data, '-->')

    def handle_entityref(self, name):
        pass
        # print('&%s;' % name)

    def handle_charref(self, name):
        pass
        # print('&#%s;' % name)
    def feed(self, data):
        return data


# def useFile(raw_data_para,out_file_para):
#     parser = MyHTMLParser()
#     with open(raw_data_para, encoding='utf-8') as raw_data, \
#             open(out_file_para, "w") as out:
#         for line in raw_data:
#             parts = line.split(" +++$+++ ")
#             dialog_line = parts[-1]
#             s = dialog_line.strip().lower()
#             p =  parser.feed(s)
#             # out.write(p)
#             # preprocessed_line = " ".join(nltk.word_tokenize(s))
#             # out.write(s + "\n")
#
# useFile('/Users/eusoft/Desktop/nyt_eng_201012','/Users/eusoft/Desktop/1.txt')

parser = MyHTMLParser()
f = open('/Users/eusoft/Desktop/nyt_eng_201012',encoding='utf8')
s = f.read()
parser.feed(s)


