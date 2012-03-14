#!/usr/bin/env python

import re
from sys import stdin,stdout,stderr

total=0
for line in stdin:
    if re.match('##',line):
        stdout.write(line)
        numbers = re.findall(r'\(([-+][0-9]+)\)',line)
        if numbers:
            for number in numbers:
                total += float(number)

stderr.write('Total: %f\n' % total)
                
