# random word generator

A small and flexible pseudorandom word generator using a markov chain.

- prwg.py:
```
NAME
    prwg

FILE
    prwg.py

CLASSES
    Prwg
    
    class Prwg
     |  @author: steampunkv@gmail.com
     |  
     |  This module allows you to analyze text files, generate a JSON file with this data and generate word based
     |  on this data
     |  
     |  Static methods defined here:
     |  
     |  analyse(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False)
     |      analyse a text file and generate data used by the generate function
     |      
     |      :param file_loc: the path to the text file you want to analyse
     |      :param datafile_name_out: the path to the JSON file where you want the data to be written
     |      :param datafile_name_in: the path to a JSON file that you want to load before you analyse anything
     |      :param over_write: write the data to the JSON FILE where you read the data from
     |      :param give_object: if you want the saveAndLoad object to be returned
     |  
     |  generate(file_in, times=1, min_word_length=0, precise_word_length=-1, random_times=(0, 0), return_string=True)
     |      generate a random word based on the JSON file generated by analyse
     |      :param file_in: path to the JSON file
     |      :param times: the amount of words you want to generate
     |      :param random_times: generate a random amount of words between the lower bound and the upper bound, these
     |      are given in a tuple with length 2
     |      :param min_word_length: the minimum length of the word
     |      :param precise_word_length: if you want to generate words with a precise length
     |      :param return_string: if you want the function to return a string instead of printing it, overwrites times and
     |      random_times
```
- saveAndLoad.py:
a help class used by prwg.py
```
NAME
    saveAndLoad

FILE
    saveAndLoad.py

CLASSES
    SaveAndLoad
    
    class SaveAndLoad
     |  @author: steampunkv@gmail.com
     |  
     |  This module allows you to save, load and add data that is useful for markov chains
     |  The file format is JSON
     |  
     |  Methods defined here:
     |  
     |  __init__(self, file_loc='')
     |  
     |  add(self, tuple_value)
     |      adds a tuple value to the data
     |      :param tuple_value: The tuple value that you want to store
     |  
     |  give_keys(self, key)
     |      :param key: the key where you want all the corresponding keys of from the dictionary associated with the key
     |      :return: an array of values containing the keys from the dictionary associated with the given key
     |  
     |  give_row(self, key)
     |      :param key: the key where you want the dictionary of
     |      :return the dictionary associated with the key
     |  
     |  give_values(self, key)
     |      :param key: the key where you want all the values of from the dictionary associated with the key
     |      :return: an array of values containing the values from the dictionary associated with the given key
     |  
     |  save_to_file(self, file_name)
     |      save the data to a JSON file
     |      :param file_name: the name of the file where the data will be written to

```
- in.py: allows you to generate a JSON file via the terminal
```
usage: in.py [-h] (-o FILE | -r FILE FILE | -w FILE) file_loc

analyses file and creates a JSON file used by out.py

positional arguments:
  file_loc      path to text file you want to analyze

optional arguments:
  -h, --help    show this help message and exit
  -o FILE       reads data from FILE and overwrites it, if the file does not
                exist it will be created
  -r FILE FILE  reads data from first arg and writes to the second
  -w FILE       writes to FILE
```

- out.py: allows you to generate pseudo random words in the terminal
```
usage: out.py [-h] [-a A | -r R R] [-m M | -l L] file_loc

generates pseudo random words based on a file generated by in.py

positional arguments:
  file_loc    the path to the .json file generated by in.py

optional arguments:
  -h, --help  show this help message and exit
  -a A        generates a set amount of pseudo random words
  -r R R      a random amount of words between the bounds given ([a,b[)
  -m M        set a minimum for the word length
  -l L        set a precise length for the pseudo random word
```
- cleanup.sh:
```
usage: cleanup.sh file_loc
```
a simple shell script to cleanup books from [project gutenberg](https://www.gutenberg.org/)
