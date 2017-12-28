#!/usr/bin/env python3
import re

from saveAndLoad import SaveAndLoad

fileLoc = input("what is the path to the file you want to analyse?: ")
fileN = open(fileLoc, "r")

overwrite_file = 'n'
file_name_in = 'standardFile.json'

load_or_not = input("Read data from existing file? [y/n]")
if load_or_not == "y":
    file_name_in = input("what is the path to the file?")
    my_obj = SaveAndLoad(file_name_in)
    overwrite_file = input('overwrite file when saving? [y/n]')
else:
    my_obj = SaveAndLoad()

if overwrite_file == 'y':
    file_name_out = file_name_in
else:
    file_name_out = input('What is the name of the file I will write my data to? (I will overwrite it)')

for line in fileN:
    line = line.split()
    for word in line:
        i = 0
        word = re.sub('[^a-zA-Z]', '', word.lower())
        my_obj.add_word_length(len(word))
        word = word.center(len(word) + 2)

        while i < len(word)-1:
            my_obj.add(word[i:i + 2])
            i += 1

my_obj.save_to_file(file_name_out)