#!/usr/bin/env python3
import random
from saveAndLoad import SaveAndLoad
previous_char = ' '
word = ''
file_in = input("path to data file: ")
my_obj = SaveAndLoad(file_in)

times = int(input("how many words?: "))
while times > 0:
    while True:
        previous_char = random.choices(my_obj.give_keys(previous_char), weights=my_obj.give_values(previous_char))[0]
        word += previous_char
        if previous_char == ' ':
            break
    print(word)
    word = ''
    times -= 1




