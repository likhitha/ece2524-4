#!/usr/bin/env python

import re
import fileinput
from sys import stderr,stdout,argv,exit

verbose=False

if len(argv) != 3:
    stderr.write("Usage: change_grade.py NAME GRADE\n")
    exit(1)
    
for line in fileinput.input('-'):
    m = re.search(argv[1], line)
    temp = line.rstrip('\n')
    if m:
        s = re.sub(r'(.*,.*,.*,).*', r'\1', temp)
	final = s + argv[2]
	print final
    else:
	print temp
