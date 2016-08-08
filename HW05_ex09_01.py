#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def print_long_words():
    document = read_file('words.txt')
    for line in document:
        for word in line.split():
            if len(word) > 20:
                print(word, "has more than 20 characters")
                
def read_file(file_name):
    """Reads a file, handles any exceptions, and returns that file
    
    Parameter:
    file_name -- the file to read"""
    try:
        document = open('words.txt', 'r')
    except (IOError, PermissionError, IsADirectoryError) as e:
        print("Something is wrong, please check the file name, or your permissions", e)
    else:
        return document

##############################################################################
def main():
    print_long_words()
    
if __name__ == '__main__':
    main()
