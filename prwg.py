#!/usr/bin/env python3
import random
from saveAndLoad import SaveAndLoad


class Prwg:
    """
    @author: steampunkv@gmail.com

    This module allows you to analyze text files, generate a JSON file with this data and generate word based
    on this data
    """

    @staticmethod
    def analyse(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False):
        """
        analyse a text file and generate data used by the generate function

        :param file_loc: the path to the text file you want to analyse
        :param datafile_name_out: the path to the JSON file where you want the data to be written
        :param datafile_name_in: the path to a JSON file that you want to load before you analyse anything
        :param over_write: write the data to the JSON FILE where you read the data from
        :param give_object: if you want the saveAndLoad object to be returned
        """
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

        # TODO: option to analyse what word length follows another

    @staticmethod
    def __generate_word(file_in, precise_word_length=-1, min_word_length=0):
        previous_char = ' '
        word = ''
        my_obj = SaveAndLoad(file_loc=file_in)

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

        return word

    @staticmethod
    def generate(file_in, times=1, min_word_length=0, precise_word_length=-1, random_times=(0, 0), return_string=True):
        """
        generate a random word based on the JSON file generated by analyse
        :param file_in: path to the JSON file
        :param times: the amount of words you want to generate
        :param random_times: generate a random amount of words between the lower bound and the upper bound, these
        are given in a tuple with length 2
        :param min_word_length: the minimum length of the word
        :param precise_word_length: if you want to generate words with a precise length
        :param return_string: if you want the function to return a string instead of printing it, overwrites times and
        random_times
        """


        if times != 1 and random_times != (0, 0):
            raise ValueError('Both \'times\' and \'random_times\' cannot be used in the same function call')
        elif random_times != (0, 0):
            lower_bound, upper_bound = random_times
            times = random.randrange(lower_bound, upper_bound)

        if return_string:
            while times > 0:
                word = Prwg.__generate_word(file_in, min_word_length=min_word_length, precise_word_length=precise_word_length)
                print(word)
                times -= 1
                word = ''
        else:
            return Prwg.__generate_word(file_in, min_word_length=min_word_length, precise_word_length=precise_word_length)

        # TODO: generate a sentence based on the the data from extra option in analyze