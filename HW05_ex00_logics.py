#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    while True:
        try:
            input_number = int(input("Please enter an integer. "))
            break
        except ValueError:
            print("Try again. Enter a non-word numeral, not a string.")
    if input_number % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print("Your number is {}.".format(odd_or_even))


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for x in range(1, 11):
        # Use 2-space formatting for single digits.
        print(x, end = "\n" if x % 10 == 0 else "  ")
   
    for x in range(11,101):
        # Use 1-space formatting for double digits.
        print(x, end = "\n" if x % 10 == 0 else " ")


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    sum_of_numbers = 0
    count = 0
    while True:
        users_input = input("Please input any number or type 'done' to quit. ")
        if users_input == "done":
            break
        else:
            try:
                input_number = int(users_input)
            except ValueError:
                print("Sorry that's not a number. Please use non-word numerals.")
            else:
                sum_of_numbers += input_number
                count += 1
    if count > 0:
        average = sum_of_numbers / count
        return average
    else:
        return
        


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print("The average of the numbers you entered is {}.".format(find_average()))

if __name__ == '__main__':
    main()
