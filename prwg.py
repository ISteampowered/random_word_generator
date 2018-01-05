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
    def analyse_word_length(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False):
        """
        analyze the text file based on word length
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
        previous_length = 0

        for line in file_in:
            line = line.split()
            for word in line:
                my_obj.add(**{previous_length: len(word)})
                previous_length = len(word)

        if datafile_name_out != '':
            my_obj.save_to_file(datafile_name_out)
        if give_object:
            return my_obj

    @staticmethod
    def analyse(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False,
                look_back_amount=1, look_forward_amount=1):

        """
        analyse a text file based on what letters follow each other
        :param file_loc: the path to the text file you want to analyse
        :param datafile_name_out: the path to the JSON file where you want the data to be written
        :param datafile_name_in: the path to a JSON file that you want to load before you analyse anything
        :param over_write: write the data to the JSON FILE where you read the data from
        :param give_object: if you want the saveAndLoad object to be returned
        :param look_back_amount: look at the n previous characters
        :param look_forward_amount: look at the n next characters
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

                word = word.lower()
                word = word.center(len(word) + 2)

                i = 0
                while i < len(word) - look_back_amount - look_forward_amount:
                    a = word[i:i + look_back_amount]
                    b = word[i + look_back_amount:i + look_back_amount + look_forward_amount]
                    my_obj.add(**{a: b})
                    i += 1

        if datafile_name_out != '':
            my_obj.save_to_file(datafile_name_out)
        if give_object:
            return my_obj

    @staticmethod
    def generate_word(file_in, precise_word_length=-1, min_word_length=0, print_to_terminal=True, **extra_files):
        """
        generates a random word
        :param file_in: path to the JSON file. This file should contain data with chunk ration of 1:1 ( if chunk length
        is 1 then this simply means what letter follows another)
        :param min_word_length: the minimum length of the word
        :param precise_word_length: if you want to generate words with a precise length
        :param print_to_terminal: print word to terminal
        :param extra_files: key value pairs where the key is the extra file location and the value is the weight you
         want to give it. The weight of file_in is one. These files may contain data with a
         lookback amount greater than 1
        :return: a pseudo random word
        """
        next_char = ' '
        word = ''
        my_obj = SaveAndLoad(file_loc=file_in)

        while True:

            chance_dict = my_obj.give_row(next_char)
            for file, weight in extra_files.items():
                look_back_amount = SaveAndLoad(file).give_lookback_amount()
                key = word[-look_back_amount:]
                chance_dict = Prwg.__combine_dicts(chance_dict, SaveAndLoad(file).give_row(key), b_weight=weight)

            next_char = random.choices(chance_dict.keys(), weights=chance_dict.values())[0]
            if next_char[-1:] != ' ':
                word += next_char

            # in case the l option is used
            if precise_word_length > 0 and len(word) == precise_word_length:
                break

            # in case the l option isn't used, the word has the minimum length and the previous character is a space
            if next_char == ' ' and min_word_length <= len(word) and precise_word_length <= 0:
                break
            else:
                continue

            # yes I know these two if statements can be combined but it is more readable this way.

        if print_to_terminal:
            print(word)
        return word

    @staticmethod
    def __combine_dicts(a, b, a_weight=1.0, b_weight=1.0):
        return dict([(k, a_weight*a.get(k, 0) + b_weight*b.get(k, 0)) for k in set(b) | set(a)])

    @staticmethod
    def generate_sentence(file_in, print_to_terminal=False, sentence_length=17, sentence_data_file='',
                          starting_word_length=5, **extra_files):
        """
        generates a sentence based on the JSON file generated by analyse
        :param file_in: path to the JSON file
        :param print_to_terminal: print sentence to terminal
        :param sentence_data_file: the path to the word length data file
        :param sentence_length: the desired length of the sentence
        :param starting_word_length: the length of the first word in the sentence
        :param extra_files: key value pairs where the key is the extra file location and the value is the weight you
         want to give it. The weight of file_in is one. These files may contain data with a lookback amount greater
         than 1
        :return pseudo random sentence
        """

        next_word_length = starting_word_length

        if sentence_data_file == '':
            raise IOError("sentence_data_file must be valid")
        else:
            sentence = ''
            sentence_obj = SaveAndLoad(sentence_data_file)
            while sentence_length > 0:
                sentence += Prwg.generate_word(file_in, precise_word_length=int(next_word_length), **extra_files)
                sentence += ' '

                next_word_length = random.choices(sentence_obj.give_keys(str(next_word_length)),
                                                  weights=sentence_obj.give_values(str(next_word_length)))[0]

                sentence_length -= 1

            if print_to_terminal:
                print(sentence)

            return sentence
