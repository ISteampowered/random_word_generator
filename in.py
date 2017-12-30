#!/usr/bin/env python3
import argparse
from prwg import Prwg

parser = argparse.ArgumentParser(description="analyses file and creates a JSON file used by out.py")

parser.add_argument('file_loc', type=str, help="path to text file you want to analyze")
parser.add_argument('-s', action='store_true', default=False,
                 help="if you want to analyze the length of the words")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-o', type=str, default='', metavar='FILE',
                   help='reads data from FILE and overwrites it, if the file does not exist it will be created')
group.add_argument('-r', type=str, default=[], nargs=2, metavar='FILE',
                   help='reads data from first arg and writes to the second')
group.add_argument('-w', type=str, default='', metavar='FILE', help='writes to FILE')
args = parser.parse_args()

fileLoc = args.file_loc

if len(args.r) == 2:
    datafile_name_in = args.r[0]
    datafile_name_out = args.r[1]
elif len(args.o) != 0:
    datafile_name_in = args.o
    datafile_name_out = datafile_name_in
else:
    datafile_name_in = ''
    datafile_name_out = args.w

Prwg.analyse(fileLoc, datafile_name_out=datafile_name_out, datafile_name_in=datafile_name_in,
             analyze_word_length=args.s)
