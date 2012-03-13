#!/usr/bin/env python2
from sys import stdout

def read_buffer_lines(buffer):
	linecount=0

	line = buffer.readline()
	while(line):
		stdout.write("line: %s" % line)
		linecount=linecount+1
		line = buffer.readline()

	stdout.write("line count: %d\n" % linecount)	

if __name__ == '__main__':
	from sys import argv,stderr,stdin

	if len(argv) > 1:
		filename=argv[1]
		stderr.write("Reading from file: %s" % filename)
		with open(filename, 'r') as buffer:
			read_buffer_lines(buffer)
	else:
		stderr.write("Reading lines from stdin")
		with stdin as buffer:
			read_buffer_lines(buffer)


