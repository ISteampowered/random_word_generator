# PRWG (Pseudo Random Word Generator)

A slightly overcomplicated and flexible pseudo random word generator using a markov chain.
Uses UTF-8.

- prwg.py:
```
NAME
    prwg

CLASSES
    builtins.object
        Prwg
    
    class Prwg(builtins.object)
     |  @author: steampunkv@gmail.com
     |  
     |  This module allows you to analyze text files, generate a JSON file with this data and generate word based
     |  on this data
     |  
     |  Static methods defined here:
     |  
     |  analyse(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False, look_back_amount=1, look_forward_amount=1)
     |      analyse a text file based on what letters follow each other
     |      :param file_loc: the path to the text file you want to analyse
     |      :param datafile_name_out: the path to the JSON file where you want the data to be written
     |      :param datafile_name_in: the path to a JSON file that you want to load before you analyse anything
     |      :param over_write: write the data to the JSON FILE where you read the data from
     |      :param give_object: if you want the saveAndLoad object to be returned
     |      :param look_back_amount: look at the n previous characters
     |      :param look_forward_amount: look at the n next characters
     |  
     |  analyse_word_length(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False)
     |      analyze the text file based on word length
     |      :param file_loc: the path to the text file you want to analyse
     |      :param datafile_name_out: the path to the JSON file where you want the data to be written
     |      :param datafile_name_in: the path to a JSON file that you want to load before you analyse anything
     |      :param over_write: write the data to the JSON FILE where you read the data from
     |      :param give_object: if you want the saveAndLoad object to be returned
     |  
     |  generate_sentence(file_in, print_to_terminal=False, sentence_length=17, sentence_data_file='', starting_word_length=5, **extra_files)
     |      generates a sentence based on the JSON file generated by analyse
     |      :param file_in: path to the JSON file
     |      :param print_to_terminal: print sentence to terminal
     |      :param sentence_data_file: the path to the word length data file
     |      :param sentence_length: the desired length of the sentence
     |      :param starting_word_length: the length of the first word in the sentence
     |      :param extra_files: key value pairs where the key is the extra file location and the value is the weight you
     |       want to give it. The weight of file_in is one. These files may contain data with a lookback amount greater
     |       than 1
     |      :return pseudo random sentence
     |  
     |  generate_word(file_in, precise_word_length=-1, min_word_length=0, print_to_terminal=False, **extra_files)
     |      generates a random word
     |      :param file_in: path to the JSON file. This file should contain data with chunk ration of 1:1 ( if chunk length
     |      is 1 then this simply means what letter follows another)
     |      :param min_word_length: the minimum length of the word
     |      :param precise_word_length: if you want to generate words with a precise length
     |      :param print_to_terminal: print word to terminal
     |      :param extra_files: key value pairs where the key is the extra file location and the value is the weight you
     |       want to give it. The weight of file_in is one. These files may contain data with a
     |       lookback amount greater than 1
     |      :return: a pseudo random word
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FILE
    prwg.py
```
- saveAndLoad.py:
a help class used by prwg.py
```
NAME
    saveAndLoad

CLASSES
    builtins.object
        SaveAndLoad
    
    class SaveAndLoad(builtins.object)
     |  @author: steampunkv@gmail.com
     |  
     |  This module allows you to save, load and add data that is useful for markov chains
     |  The file format is JSON
     |  
     |  Methods defined here:
     |  
     |  __init__(self, file_loc='')
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add(self, **tuple_values)
     |      adds a tuple value to the data
     |      :param tuple_values: The tuple values that you want to store
     |  
     |  combine_self(self, *datafiles_name_in)
     |  
     |  give_dictionary(self)
     |  
     |  give_keys(self, key)
     |      :param key: the key where you want all the corresponding keys of from the dictionary associated with the key
     |      :return: an array of values containing the keys from the dictionary associated with the given key
     |  
     |  give_lookback_amount(self)
     |      :return: N from N:M if N is the same for the whole file
     |  
     |  give_lookforward_amount(self)
     |      :return: M from N:M if M is the same for the while file
     |  
     |  give_row(self, key)
     |      :param key: the key where you want the dictionary of
     |      :return the dictionary associated with the key
     |  
     |  give_values(self, key)
     |      :param key: the key where you want all the values of from the dictionary associated with the key
     |      :return: an array of values containing the values from the dictionary associated with the given key
     |  
     |  pretty_print(self)
     |      prints the data contained in this object in a tab seperated way, usefull for importing it in a
     |      spreadsheet program. (spoilers: it probably wont actually look anywhere near pretty in the console
     |  
     |  save_to_file(self, file_name)
     |      save the data to a JSON file
     |      :param file_name: the name of the file where the data will be written to
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  combine(datafile_name_out='', *datafiles_name_in)
     |      combines two or more datafiles
     |      :param  datafile_name_out: the name of the JSON file where the combined data will be stored
     |      :param  datafiles_name_in: all the datafiles you want to combine
     |      :return returns an SaveAndLoad object that contains the merged data from all datafiles
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FILE
    saveAndLoad.py
```
- in.py: allows you to generate a JSON file via the terminal
```
usage: in.py [-h] [-s | -l L] (-o | -r FILE) file_loc datafile_name

analyses file and creates a JSON file used by out.py

positional arguments:
  file_loc              path to text file you want to analyze
  datafile_name         path to JSON file where you want the data to be
                        written

optional arguments:
  -h, --help            show this help message and exit
  -s, --analyze-length  if you want to analyze the length of the words
  -l L, --look-back-amount L
                        sets the look back
  -o, --over-write      reads data from datafile_name and overwrites it, if
                        the file does not exist it will be created
  -r FILE, --read-from FILE
                        reads data from FILE
```

- out.py: allows you to generate pseudo random words in the terminal
```
usage: out.py [-h] [-s sentence_file] [-t T] [-w W] [-a A | -r R R]
              [-m M | -l L]
              file_loc

generates pseudo random words based on a file generated by in.py

positional arguments:
  file_loc              the path to the .json file generated by in.py

optional arguments:
  -h, --help            show this help message and exit
  -s sentence_file, --sentence sentence_file
                        generate a sentence instead of just a word it will
                        overwrite all other settings. The -f option has to be
                        set when using this
  -t T, --sentence-length T
                        set a precise sentence length, only required if the -s
                        option is used
  -w W, --sentence-starting-word-length W
                        starting word length, only needed if the -s option is
                        used
  -a A, --pseudo-random-word-amount A
                        generates a set amount of pseudo random words
  -r R R, --random-amount R R
                        a random amount of words between the bounds given
                        ([a,b[)
  -m M, --minimum-word-length M
                        set a minimum for the word length
  -l L, --word-length L
                        set a precise length for the pseudo random word
```
- cleanup.sh:
```
usage: cleanup.sh file_loc
```
a simple shell script to cleanup plain text files from [project gutenberg](https://www.gutenberg.org/)

the three json files where generated based on english text with 1, 2 and 3 as lookback amount