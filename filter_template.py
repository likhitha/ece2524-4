#!/usr/bin/env python2
import fileinput
from sys import stderr,stdout

for line in fileinput.input():
	if fileinput.isfirstline():
		stderr.write("Reading from %s\n" % fileinput.filename())
	stdout.write("line: %s" % line)
