#!/usr/bin/env python

import operator
import sys

global dictionary
dictionary = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    site, count = line.split('\t', 1)
    
    # store in the dictionary the values
    dictionary[site] = int(count)

#get the list of ordered keys
i = 1
for key, value in sorted(dictionary.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)
    if(i > 10):
    	break
    i = i + 1