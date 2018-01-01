# PRWG (Pseudo Random Word Generator)

A slightly overcomplicated and flexible pseudo random word generator using a markov chain.

- prwg.py:
```
Help on module prwg:

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
     |  analyse(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False, look_back_amount=1)
     |      analyse a text file based on what letters follow each other
     |      
     |      :param file_loc: the path to the text file you want to analyse
     |      :param datafile_name_out: the path to the JSON file where you want the data to be written
     |      :param datafile_name_in: the path to a JSON file that you want to load before you analyse anything
     |      :param over_write: write the data to the JSON FILE where you read the data from
     |      :param give_object: if you want the saveAndLoad object to be returned
     |      :param look_back_amount: look at the n previous characters
     |  
     |  analyse_word_length(file_loc, datafile_name_out='', over_write=False, datafile_name_in='', give_object=False)
     |      analyze the text file based on word length
     |      
     |      :param file_loc: the path to the text file you want to analyse
     |      :param datafile_name_out: the path to the JSON file where you want the data to be written
     |      :param datafile_name_in: the path to a JSON file that you want to load before you analyse anything
     |      :param over_write: write the data to the JSON FILE where you read the data from
     |      :param give_object: if you want the saveAndLoad object to be returned
     |  
     |  generate(file_in, min_word_length=0, precise_word_length=-1, return_string=True, generate_sentence=False, sentence_length=17, sentence_data_file='', starting_word_length=5)
     |      generate a random word based on the JSON file generated by analyse
     |      :param file_in: path to the JSON file
     |      :param min_word_length: the minimum length of the word
     |      :param precise_word_length: if you want to generate words with a precise length
     |      :param return_string: if you want the function to return a string instead of printing it, overwrites times and
     |      random_times
     |      :param generate_sentence: if you want to generate a sentence, requires the sentence_data_file to be set
     |      :param sentence_data_file: the path to the word length data file
     |      :param sentence_length: the disered length of the sentence
     |      :param starting_word_length: the length of the first word in the sentence
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
Help on module saveAndLoad:

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
     |  give_dictionary(self)
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
     |  pretty_print(self)
     |      prints the data contained in this object in a tab seperated way, usefull for importing it in a
     |      spreadsheet program. (spoilers: it probably wont actually look anywhere near pretty in the console
     |  
     |  save_to_file(self, file_name)
     |      save the data to a JSON file
     |      :param file_name: the name of the file where the data will be written to
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
usage: in.py [-h] [-s] (-o FILE | -r FILE FILE | -w FILE) file_loc

analyses file and creates a JSON file used by out.py

positional arguments:
  file_loc      path to text file you want to analyze

optional arguments:
  -h, --help    show this help message and exit
  -s            if you want to analyze the length of the words
  -o FILE       reads data from FILE and overwrites it, if the file does not
                exist it will be created
  -r FILE FILE  reads data from first arg and writes to the second
  -w FILE       writes to FILE
```

- out.py: allows you to generate pseudo random words in the terminal
```
usage: out.py [-h] [-s] [-t T] [-f F] [-w W] [-a A | -r R R] [-m M | -l L]
              file_loc

generates pseudo random words based on a file generated by in.py

positional arguments:
  file_loc    the path to the .json file generated by in.py

optional arguments:
  -h, --help  show this help message and exit
  -s          generate a sentence instead of just a word it will overwrite all
              other settings. The -f option has to be set when using this
  -t T        set a precise sentence length, only required if the -s option is
              used
  -f F        sentence file location, only needed if -s option is used
  -w W        starting word length, only needed if the -s option is used
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
