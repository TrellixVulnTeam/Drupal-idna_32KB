#!/usr/bin/python

import requests
import re
import sys
try:
        # print sys.argv[1];
        url = 'https://www.facebook.com/' + sys.argv[1]
        idre = re.compile('"entity_id":"([0-9]+)"')
        page = requests.get(url)
        print idre.findall(page.content)
except:
    print "Unexpected error:", sys.exc_info()[0]