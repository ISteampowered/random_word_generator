#!/usr/bin/env python3
import re
import argparse
from saveAndLoad import SaveAndLoad

parser = argparse.ArgumentParser(description="analyses file and creates a JSON file used by out.py")

parser.add_argument('file_loc', type=str, help="path to text file you want to analyze")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-o', type=str, default='', metavar='FILE',  help='reads data from FILE and overwrites it, if the '
                                                                     'file does not exist it will be created')
group.add_argument('-r', type=str, default=[], nargs=2, metavar='FILE', help='reads data from first arg and writes to '
                                                                             'the second')
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

my_obj = SaveAndLoad(datafile_name_in)

fileN = open(fileLoc, "r")


for line in fileN:
    line = line.split()
    for word in line:
        i = 0
        word = re.sub('[^a-zA-Z]', '', word.lower())
        word = word.center(len(word) + 2)

        while i < len(word)-1:
            my_obj.add(word[i:i + 2])
            i += 1


my_obj.save_to_file(datafile_name_out)
