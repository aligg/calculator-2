"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def reduce(function, iterable, initializer=None):
    """doc string here"""
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

calculator_on = True

while calculator_on:
    tokenized_list = raw_input("Enter numbers or enter 'q' to quit: ").split()
    symbol = tokenized_list[0]
    augmented_list = tokenized_list[1:]
    int_list=[]
    for i in augmented_list:
        i = int(i)
        int_list.append(i)

    # if len(tokenized_list) > 1:
    #     num1 = int(tokenized_list[1])
    # if len(tokenized_list) > 2:
    #     num2 = int(tokenized_list[2])
    # if len(tokenized_list) > 3:
    #     num3 = int(tokenized_list[3])
    # if len(tokenized_list) > 4:
    #     print "Only returning results for first three inputs"

    if symbol.lower() == 'q':
        calculator_on = False
        print "You're now exiting the calculator. Bye Felicia"

    elif symbol == '+':
        print reduce(add, int_list)
    elif symbol == '-':
        print reduce(subtract, int_list)
    elif symbol == '*':
        print reduce(multiply, int_list)
    elif symbol == '/':
        # if num2 == 0:
        #     print "You can't divide by zero"
        #     continue
        print reduce(divide, int_list)
    elif symbol == "pow":
        print reduce(power, int_list)
    elif symbol == "mod":
        print reduce(mod, int_list)
    # elif symbol == "cubes+":
    #     print reduce(add_cubes, int_list)
    # elif symbol == "x+":
    #     print reduce(add_mult, int_list)
    elif symbol == "square":
        print reduce(square, int_list)
    elif symbol == "cube":
        print reduce(cube, int_list)
    else:
        print "Bad input, try again please."
        continue
