#!/usr/bin/env python3
import json


class SaveAndLoad:

    """
    @author: steampunkv@gmail.com

    This module allows you to save, load and add data that is useful for markov chains
    The file format is JSON
    """

    def add(self, **tuple_values):
        """
        adds a tuple value to the data
        :param tuple_values: The tuple values that you want to store
        """
        for key, value in tuple_values.items():
            row = self.give_row(key)
            row[value] = row.get(value, 0) + 1
            self.big_list[key] = row

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

    @staticmethod
    def __combine_dicts(a, b):
        return dict(list(a.items()) + list(b.items()) + [(k, a[k] + b[k]) for k in set(b) & set(a)])

    def combine_self(self, *datafiles_name_in):

        for datafile_name_in in datafiles_name_in:
            merge_file_obj = SaveAndLoad(datafile_name_in)
            for key in merge_file_obj.give_dictionary().keys():
                self.__combine_row(key, merge_file_obj.give_row(key))

    def __combine_row(self, key, row):
        self.big_list[key] = self.__combine_dicts(self.big_list.get(key, {}), row)

    @staticmethod
    def combine(datafile_name_out='', *datafiles_name_in):
        """
        combines two or more datafiles
        :param  datafile_name_out: the name of the JSON file where the combined data will be stored
        :param  datafiles_name_in: all the datafiles you want to combine
        :return returns an SaveAndLoad object that contains the merged data from all datafiles
        """

        if len(datafiles_name_in) < 2:
            raise IOError('at least 2 file must be given in order to merge')

        datafiles_name_in = list(datafiles_name_in)
        save_and_load_obj = SaveAndLoad(datafiles_name_in[0])
        datafiles_name_in.pop(0)

        save_and_load_obj.combine_self(*datafiles_name_in)

        if datafile_name_out != '':
            save_and_load_obj.save_to_file(datafile_name_out)

        return save_and_load_obj

        # TODO: update readme

    __n_value = -1
    __m_value = -1

    def give_N(self):
        """
        :return: N from N:M if N is the same for the whole file
        """
        if self.__n_value == -1:
            previous_key_length = len(list(self.big_list.keys())[0])
            for key in self.big_list.keys():
                if len(key) != previous_key_length:
                    raise TypeError('N is not the same for the whole file')

            self.__n_value = previous_key_length

        return self.__n_value

    def give_M(self):
        """
        :return: M from N:M if M is the same for the while file
        """
        if self.__m_value == -1:
            previous_value_length = len(list((list(self.big_list.values())[0]).keys())[0])
            #gives the length of the first key in the first dictionary containted in big_list
            for dict in self.big_list.values():
                for key in dict:
                    if len(key) != previous_value_length:
                        raise TypeError('M is not the same for the whole file')

            self.__m_value = previous_value_length

        return self.__m_value