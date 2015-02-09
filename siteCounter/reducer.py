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
	domain, count, size, fullreqtime = line.split('\t', 3)
	count = int(count)
	size = int(size)
	fullreqtime = int(fullreqtime)
	if domain in dictionary:
		values = dictionary[domain]
		count = count + values[0]
		size = size + values[1]
		fullreqtime = fullreqtime + values[2]
	# store in the dictionary the values
	dictionary[domain] = [count, size, fullreqtime]

#get the list of ordered keys
i = 1
for key, value in sorted(dictionary.iteritems(), key=lambda (k,v): (v,k), reverse=True):
	#calculate avgs
	values = dictionary[key]
	avg_size = float(value[1])/float(value[0])
	avg_fullreqtime = float(value[2])/float(value[0])
	print "%s: %s, %s, %s" % (key, value[0], avg_size, avg_fullreqtime)
	if(i > 10):
		break
	i = i + 1