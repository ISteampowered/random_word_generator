#!/usr/bin/env python3
import argparse
import random
from prwg import Prwg
parser = argparse.ArgumentParser(description="generates pseudo random words based on a file generated by in.py")

parser.add_argument('file_loc', help='the path to the .json file generated by in.py')
over_arching_group = parser.add_mutually_exclusive_group()

over_arching_group.add_argument('-s', '--sentence', dest='s', default='', type=str, metavar='sentence_file',
                                help='generate a sentence instead of just a word it will overwrite all other settings. '
                                     'The -f option has to be set when using this')

parser.add_argument('-t', '--sentence-length', dest='t',  default=17, type=int,
                    help='set a precise sentence length, only required if the -s option is used')
parser.add_argument('-w', '--sentence-starting-word-length', dest='w', default=5, type=int,
                    help='starting word length, only needed if the -s option is used')

group2 = over_arching_group.add_mutually_exclusive_group()
group2.add_argument('-a', '--pseudo-random-word-amount',dest='a', type=int, default=1,
                    help='generates a set amount of pseudo random words')
group2.add_argument('-r', '--random-amount', dest='r', type=int, nargs=2, default=[1, 1],
                    help='a random amount of words between the bounds given ([a,b[)')

group = over_arching_group.add_mutually_exclusive_group()
group.add_argument('-m', '--minimum-word-length',dest='m', type=int, default=0, help='set a minimum for the word length')
group.add_argument('-l', '--word-length', dest='l', type=int, default=-1, help='set a precise length for the pseudo random word')

args = parser.parse_args()

file_in = args.file_loc

if args.s != '':
    Prwg.generate_sentence(file_in, print_to_terminal=True, sentence_data_file=args.s,
                           sentence_length=args.t, starting_word_length=args.w)
    exit(0)

min_word_length = args.m

if args.a != 1:
    times = args.a
elif args.r[0] != 1 and args.r[1] != 1:
    times = random.randrange(args.r[0], args.r[1])
else:
    times = 1

while times > 0:
    Prwg.generate_word(file_in, min_word_length=min_word_length, precise_word_length=args.l, print_to_terminal=True)
    times -= 1
