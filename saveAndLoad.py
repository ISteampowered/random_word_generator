#!/usr/bin/env python3
import json


class SaveAndLoad:

    """
    @author: steampunkv@gmail.com

    This module allows you to save, load and add data that is useful for markov chains
    The file format is JSON
    """

    def add(self, tuple_value):
        """
        adds a tuple value to the data
        :param tuple_value: The tuple value that you want to store
        """
        first_letter, second_letter = tuple_value
        row = self.big_list.get(first_letter, {})
        row[second_letter] = row.get(second_letter, 0) + 1
        self.big_list[first_letter] = row

    def save_to_file(self, file_name):
        """
        save the data to a JSON file
        :param file_name: the name of the file where the data will be written to
        """
        with open(file_name, 'w') as output_file:
            json.dump(self.big_list, output_file, sort_keys=True, indent=4)

    def __load_from_file(self, file_name):
        """
        load data from a JSON file, this overwrites the data that is currently stored in the object
        :param file_name: the name of the file where you want to load the data from
        """
        with open(file_name) as fileN:
            self.big_list = json.load(fileN)

    def __init__(self, file_loc=''):
        self.big_list = {}
        if file_loc != '':
            self.__load_from_file(file_loc)

    def give_row(self, key):
        """
        :param key: the key where you want the dictionary of
        :return the dictionary associated with the key
        """
        return self.big_list.get(key, {})

    def give_keys(self, key):
        """
        :param key: the key where you want all the corresponding keys of from the dictionary associated with the key
        :return: an array of values containing the keys from the dictionary associated with the given key
        """
        return list(self.give_row(key).keys())

    def give_values(self, key):
        """
        :param key: the key where you want all the values of from the dictionary associated with the key
        :return: an array of values containing the values from the dictionary associated with the given key
        """
        return list(self.give_row(key).values())

    def pretty_print(self):
        """
        prints the data contained in this object in a tab seperated way, usefull for importing it in a
        spreadsheet program. (spoilers: it probably wont actually look anywhere near pretty in the console
        """
        keys = list(self.big_list.keys())
        keys2 = keys.copy()
        for key in keys:
            keys2 += self.give_keys(key)
        keys = list(set(keys2))
        keys.sort()
        print('\t', end='')
        for key in keys:
            print(key, end='\t')
        print()
        for key in keys:
            print(key, end='\t')
            for key2 in keys:
                print(self.big_list.get(key, {}).get(key2, 0), end='\t')
            print()

    def give_dictionary(self):
        return self.big_list

