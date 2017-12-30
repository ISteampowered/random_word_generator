#!/usr/bin/env python3
import random
from saveAndLoad import SaveAndLoad


class Prwg:

    @staticmethod
    def analyse(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False):

        if over_write:
            datafile_name_out = datafile_name_in

        if datafile_name_out == '' and not give_object:
            raise IOError('No data output given.')

        my_obj = SaveAndLoad(file_loc=datafile_name_in)
        file_in = open(file_loc, "r")

        for line in file_in:
            line = line.split()
            for word in line:
                i = 0
                word = word.lower()
                word = word.center(len(word) + 2)

                while i < len(word)-1:
                    my_obj.add(word[i:i + 2])
                    i += 1

        if datafile_name_out != '':
            my_obj.save_to_file(datafile_name_out)
        if give_object:
            return my_obj

    @staticmethod
    def generate(file_in, times=1, min_word_length=0, precise_word_length=-1, random_times=(0, 0)):

        previous_char = ' '
        word = ''
        my_obj = SaveAndLoad(file_loc=file_in)

        if times != 1 and random_times != (0, 0):
            raise ValueError('Both \'times\' and \'random_times\' cannot be used in the same function call')
        elif random_times != (0, 0):
            lower_bound, upper_bound = random_times
            times = random.randrange(lower_bound, upper_bound)

        while times > 0:
            while True:
                previous_char = random.choices(my_obj.give_keys(previous_char),
                                               weights=my_obj.give_values(previous_char))[0]
                if previous_char != ' ':
                    word += previous_char

                # in case the l option is used
                if precise_word_length > 0 and len(word) == precise_word_length:
                    break

                # in case the l option isn't used, the word has the minimum length and the previous character is a space
                if previous_char == ' ' and min_word_length <= len(word) and precise_word_length <= 0:
                    break
                else:
                    continue

                # yes I know these two if statements can be combined but it is more readable this way.

            print(word)
            times -= 1
            word = ''
