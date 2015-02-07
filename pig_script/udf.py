#!/usr/bin/env python
from urlparse import urlparse
from pig_util import outputSchema

@outputSchema("url")
def extractSite(url):
    domain = ""
    if url:
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain

@outputSchema("size")
def transform(value,magnitude):
    magn = 1
    if (magnitude.strip()).upper()=='B':
        magn = 1
    else:
        if (magnitude.strip()).upper()=='KB':
            magn = 1024
    value = int(value)/magn
    return value