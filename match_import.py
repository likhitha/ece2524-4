#!/usr/bin/env python

import match_action
from sys import stdin,stdout

(total, comments) = match_action.comment_parse(stdin)

stdout.write(comments)
stdout.write("Total: %d\n" % total)
