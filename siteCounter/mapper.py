#!/usr/bin/env python

import sys
from urlparse import urlparse

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('parameters.ini')

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

def process(line, magnitude):
    # transform line into dictionary
    dictionary = lineDictionary(line)
    #take values requested
    try:
        url = dictionary['url']
        size = dictionary['size']
        fullreqtime = dictionary['fullreqtime']

        #convert values to order of magnitude chose
        if magnitude == 'KB':
            magn = 1
        else:
            if magnitude == 'MB':
                magn = 1024

        size = int(size)/magn
        fullreqtime = int(fullreqtime)/magn


        site = extractSite(url)
        globantDom = "globant.com";
        res = site.find(globantDom);
        if(res == -1):
            print '%s\t%s\t%s\t%s' % (site, 1, size, fullreqtime)
    except:
        return

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    magnitude = parser.get('parameters', 'magnitude')
    process(line, magnitude)