#!/usr/bin/env python3
import random
from saveAndLoad import SaveAndLoad

previous_char = ' '
word = ''
file_in = input("path to data file: ")
my_obj = SaveAndLoad(file_in)

times = int(input("how many words?: "))
min_word_length = int(input("what is the minimum word legnth?"))
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




