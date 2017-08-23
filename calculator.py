"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

# do_setup()
# while exit_condition_not_reached:
#     input = consume_input()
#     output = evaluate_input(input)
#     print output



from arithmetic import *

# Your code goes here
calculator_on = True

while calculator_on:
    tokenized_list = raw_input("Enter numbers or enter 'q' to quit: ").split()
    if len(tokenized_list) > 1:
        num1 = int(tokenized_list[1])
    if len(tokenized_list) > 2:
        num2 = int(tokenized_list[2])
    if len(tokenized_list) > 3:
        num3 = int(tokenized_list[3])

    symbol = tokenized_list[0]
    if symbol == 'q' or symbol == 'Q':
        calculator_on = False
        print "You're now exiting the calculator. Bye Felicia"

    elif symbol == '+':
        print add(num1, num2)
    elif symbol == '-':
        print subtract(num1, num2)
    elif symbol == '*':
        print multiply(num1, num2)
    elif symbol == '/':
        if num2 == 0:
            print "You can't divide by zero"
            continue
        print divide(num1, num2)
    elif symbol == "pow":
        print power(num1, num2)
    elif symbol == "mod":
        print mod(num1, num2)
    elif symbol == "cubes+":
        print add_cubes(num1, num2)
    elif symbol == "x+":
        print add_mult(num1, num2, num3)
    elif symbol == "square":
        print square(num1)
    elif symbol == "cube":
        print cube(num1)
