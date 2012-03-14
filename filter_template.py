#!/usr/bin/env python2
import fileinput
from sys import stderr,stdout

for line in fileinput.input():
	if fileinput.isfirstline():
		stderr.write("\033[1;31mReading from %s\033[0m\n" % fileinput.filename())
	stdout.write("line: %s" % line)
