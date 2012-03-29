#!/usr/bin/env python

import re

def comment_parse(data):
    """scan through lines of data.  Generate a comments blob containing all lines starting with '##'.
        If a line starts with '##' and contains a number in parenthasis, then add the value of that number to a running total."""
        
    comments=""
    total=0
    for line in data:
        if re.match('##',line):
            comments += line
            numbers = re.findall(r'\(([-+][0-9]+)\)',line)
            if numbers:
                for number in numbers:
                    total += float(number)
    return (total, comments)
  
if __name__=='__main__':
    from sys import stdin,stdout,stderr
    
    (total, comments) = comment_parse(stdin)
    stderr.write(comments)
    stderr.write('Total: %f\n' % total)
                
