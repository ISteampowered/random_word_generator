#!/usr/bin/env python3
import argparse
from prwg import Prwg

parser = argparse.ArgumentParser(description="analyses file and creates a JSON file used by out.py")

parser.add_argument('file_loc', type=str, help="path to text file you want to analyze")
parser.add_argument('datafile_name', type=str, help='path to JSON file where you want the data to be written')

group2 = parser.add_mutually_exclusive_group()
group2.add_argument('-s', '--', action='store_true', default=False,
                    help="if you want to analyze the length of the words")
group2.add_argument('-l', '--look-back-amount', type=int, default=1, help='sets the look back')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-o', '--over-write', action='store_true', default=False,
                   help='reads data from datafile_name and overwrites it, if the file does not exist it will be created')
group.add_argument('-r', '--read-from', type=str, default='', metavar='FILE', help='reads data from FILE')
args = parser.parse_args()

# TODO: add double dash flags
fileLoc = args.file_loc
datafile_name_out = args.datafile_name
datafile_name_in = ''

if args.o:
    datafile_name_in = args.datafile_name
elif args.r != '':
    datafile_name_in = args.r


if args.s:
    Prwg.analyse_word_length(fileLoc, datafile_name_out=datafile_name_out, datafile_name_in=datafile_name_in)
else:
    Prwg.analyse(fileLoc, datafile_name_out=datafile_name_out, datafile_name_in=datafile_name_in,
                 look_back_amount=args.l)

