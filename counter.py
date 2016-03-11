""" A program that stores and updates a counter using a Python pickle file.

For the Olin College Software Design class. 
Script skeleton and doctests provided.

@Author Elizabeth Sundsmo 3/10/2016
"""

from os.path import exists
import sys
from pickle import dump, load

def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

        A new counter will be created and initialized to 1 if none exists or if
        the reset flag is True.

        If the counter already exists and reset is False, the counter's value will
        be incremented.

        file_name: the file that stores the counter to be incremented.  If the file
                   doesn't exist, a counter is created and initialized to 1.
        reset: True if the counter in the file should be rest.
        returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    
    #if the file already exists increment the existing counter
    if exists(file_name) and reset==False:
        #open the given file in reading plus writing mode ('r+')
        open_file= open(file_name, 'r+')
        #load the contents of the opened file into file_counter
        file_counter = load(open_file) 
        #increment the contents (stored as int)
        file_counter+=1 
        #move handle to start so old value will be overwritten in dump
        open_file.seek(0,0)
        #writes the new file_counter value into the open file
        dump(file_counter, open_file)

    #otherwise it doesn't exist so set the file counter to 1
    else:
        #open the given file in writing mode ('w')
        #(OVERWRITES ANY EXISTING FILE OF SAME NAME)
        open_file= open(file_name, 'w')
        #set counter to 1 (type int)
        file_counter=1
        #write this value into the empty open file
        dump(file_counter, open_file)

    #ALWAYS CLOSE YOUR FILES WHEN YOU ARE DONE WITH THEM
    open_file.close

    #return the current value of the counter for doctesting and print statement
    return file_counter


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod(verbose=True)
    else:
        print "new value is " + str(update_counter(sys.argv[1]))