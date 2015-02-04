#!/usr/bin/env python

import sys
from urlparse import urlparse

#This algorithm is taking off 
#http://stackoverflow.com/questions/1644362/best-way-to-parse-a-line-in-python-to-a-dictionary
def lineDictionary(string):
    inside_quotes = False
    key = None
    value = ""
    dict = {}

    for c in string:
        if c == '"':
            inside_quotes = not inside_quotes
        elif c == '=' and not inside_quotes:
            key = value
            value = ''
        elif c == ' ':
            if inside_quotes:
                value += ' ';
            elif key and value:
                dict[key] = value
                key = None
                value = ''
        else:
            value += c

    dict[key] = value
    return dict

def extractSite(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # transform line into dictionary
    dictionary = lineDictionary(line)
    url = dictionary['url']
    site = extractSite(url) 
    print '%s\t%s' % (site, 1)