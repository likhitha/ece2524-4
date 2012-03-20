#!/usr/bin/env python

import re
import fileinput
from sys import stderr,stdout,argv,exit

verbose=False
def main():
	if len(argv) != 3:
		stderr.write("Usage: change_grade.py NAME GRADE\n")
		exit(1)
	change(argv[1], argv[2])

	
def change ( name, grade ):
	for line in fileinput.input('-'):
		m = re.search(name, line)
		temp = line.rstrip('\n')
		if m:
			s = re.sub(r'(.*,.*,.*,).*', r'\1', temp)
			final = s + grade
			print final
		else:
			print temp
	return 0

if __name__ == "__main__":
	main()