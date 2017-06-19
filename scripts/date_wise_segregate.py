# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:59:08 2017

@author: jagadeesh
"""

fp = open("comsetup.log")

import re

pattern = re.compile("\d{2},\d{2},\d{4}")

for line in fp:
    matches = pattern.serach(line)
    if not matches is None:
        print(matches.group())
        