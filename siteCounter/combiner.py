#!/usr/bin/env python

from operator import itemgetter
import sys

current_domain = None
current_count = 0
current_size = 0
current_fullreqtime = 0
domain = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    domain, count, size, fullreqtime = line.split('\t', 3)

    # convert count (currently a string) to int
    try:
        count = int(count)
        size = int(size)
        fullreqtime = int(fullreqtime)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: domain) before it is passed to the reducer
    if current_domain == domain:
        current_count += count
        current_size += size
        current_fullreqtime += fullreqtime
    else:
        if current_domain:
            # write result to STDOUT
            print '%s\t%s\t%s\t%s' % (current_domain, current_count,current_size, current_fullreqtime)
        current_count = count
        current_size = size
        current_fullreqtime = fullreqtime
        current_domain = domain

# do not forget to output the last domain if needed!
if current_domain == domain:
    print '%s\t%s\t%s\t%s' % (current_domain, current_count,current_size, current_fullreqtime)