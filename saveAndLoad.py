#!/usr/bin/env python3
import json


class SaveAndLoad:

    def add(self, two_letters):
        first_letter, second_letter = two_letters
        row = self.big_list.get(first_letter, {})
        row[second_letter] = row.get(second_letter, 0) + 1
        self.big_list[first_letter] = row

    def save_to_file(self, file_name):
        with open(file_name, 'w') as output_file:
            json.dump(self.big_list, output_file, sort_keys=True, indent=4)

    def __load_from_file(self, file_name):
        with open(file_name) as fileN:
            self.big_list = json.load(fileN)

    def __init__(self, file_loc=''):
        self.big_list = {}
        if file_loc != '':
            self.__load_from_file(file_loc)

    def print_self(self):
        print(self.big_list)

    def __give_row(self, letter):
        return self.big_list.get(letter, {})

    def give_keys(self, letter):
        return list(self.__give_row(letter).keys())

    def give_values(self, letter):
        return list(self.__give_row(letter).values())