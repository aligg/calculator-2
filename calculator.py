"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def my_reduce(function, number_list):
    """ Reduces the items in a list allowing calc to process multiple numbers"""
    av = number_list[0]
    if len(number_list) == 1:
        for number in number_list:
            av = function(av)
    else:
        for number in number_list[1:]:
            av = function(av, number)
    return av

calculator_on = True

while calculator_on:
    tokenized_list = raw_input("Enter numbers or enter 'q' to quit: ").split()
    symbol = tokenized_list[0]
    augmented_list = tokenized_list[1:]
    int_list=[]
    for i in augmented_list:
        i = int(i)
        int_list.append(i)

    if symbol.lower() == 'q':
        calculator_on = False
        print "You're now exiting the calculator. Bye Felicia"

    elif symbol == '+':
        print my_reduce(add, int_list)
    elif symbol == '-':
        print my_reduce(subtract, int_list)
    elif symbol == '*':
        print my_reduce(multiply, int_list)
    elif symbol == '/':
        # if num2 == 0:
        #     print "You can't divide by zero"
        #     continue
        print my_reduce(divide, int_list)
    elif symbol == "pow":
        print my_reduce(power, int_list)
    elif symbol == "mod":
        print my_reduce(mod, int_list)
    # elif symbol == "cubes+":
    #     print reduce(add_cubes, int_list)
    # elif symbol == "x+":
    #     print reduce(add_mult, int_list)
    elif symbol == "square":
        print my_reduce(square, int_list)
    elif symbol == "cube":
        print my_reduce(cube, int_list)
    else:
        print "Bad input, try again please."
        continue
