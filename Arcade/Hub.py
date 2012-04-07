#!/usr/bin/python

from sys import stdin, stdout
import argparse
import os.path
import csv
from collections import OrderedDict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('values', metavar='N', nargs='+',
                        help='Arguments for the flags')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', dest='action', action='store_const',
                       const='list', default='none', 
                       help='game num --list : List the first '
                       'num entries of game')
    group.add_argument('--add', dest='action', action='store_const',
                       const='add', default='none',
                       help='game user score --add : Add user '
                       'and score to game leaderboard')
    group.add_argument('--del', dest='action', action='store_const',
                       const='del', default='none',
                       help='game [user] --del : Delete game or '
                       'user from game leaderboards')
    args = parser.parse_args()
    
    filename = args.values[0] + ".csv"
    #need error checking for if file doesnt exist
    if os.path.exists(filename) is False:
        fd = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
        f = os.fdopen(fd)
        f.close()   
    score_list = {}
    """ Parse the contents of the file into a dict for user/score """
    ifile = open(filename, "rb")
    reader = csv.reader(ifile)
    for row in reader:
        score_list[row[0]] = row[1]
    ifile.close()
    """ Perform action requested """
    if args.action is "del":
        if len(args.values) == 1:
            if os.path.exists(filename):
                os.remove(filename)
        elif len(args.values) == 2:
            #need error checking for if username isnt there
            del score_list[args.values[1]]
            ofile = open(filename, "w")
            writer = csv.writer(ofile, delimiter=",")
            for keyv in score_list:
                writer.writerow([keyv, score_list[keyv]])
            ofile.close()
        else:
            print "Error handling here"
    elif args.action is "add":
        if len(args.values) == 3:
            try:
                nscore = int(args.values[2])
                if score_list.has_key(args.values[1]):
                    if nscore > int(score_list[args.values[1]]):
                        score_list[args.values[1]] = nscore
                else:
                    score_list[args.values[1]] = nscore
            except ValueError:
                print "Score must be an integer value"
            ofile = open(filename, "w")
            writer = csv.writer(ofile, delimiter=",")
            for keyv in score_list:
                writer.writerow([keyv, score_list[keyv]])
            ofile.close()
        else:
            print "Error handling here"
    elif args.action is "list":
        if len(args.values) == 2: 
            sorted_list = OrderedDict(sorted(score_list.items(), key=lambda t: t[1], reverse=False))
            count = 0
            max = 0
            try:
                max = int(args.values[1])
                if max > len(score_list):
                    max = len(score_list)
            except ValueError:
                print "Number must be an integer value"
            writer = csv.writer(stdout, delimiter="\t")
            while count < max:
                keyv = sorted_list.popitem()
                writer.writerow([keyv[0], keyv[1]])
                count = count + 1
        else:
            print "Error handling here"
        
if __name__ == "__main__":
    main()

    
