#!/usr/bin/env python3
import random
import sys
from saveAndLoad import SaveAndLoad

previous_char = ' '
word = ''
if len(sys.argv) == 1:
    file_in = input("path to data file: ")
    times = int(input("how many words?: "))
    min_word_length = int(input("what is the minimum word length?"))

elif len(sys.argv) == 4:
    file_in = sys.argv[1]
    times = int(sys.argv[2])
    min_word_length = int(sys.argv[3])
else:
    print("Syntax: {} {} {} {}".format(sys.argv[0], 'file_path', 'amount_of_words', 'min_word_length'))

my_obj = SaveAndLoad(file_in)

while times > 0:
    while True:
        previous_char = random.choices(my_obj.give_keys(previous_char), weights=my_obj.give_values(previous_char))[0]
        word += previous_char
        if previous_char == ' ':
            break
    if min_word_length <= len(word):
        print(word)
        times -= 1
    word = ''




